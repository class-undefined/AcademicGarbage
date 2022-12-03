from typing import List, Tuple, Dict
from common.error import RequestError
from common.response import Response
from db import mongodb
from db.photo import Photo
from common.package import encode_data, random_string, encode_md5_from_string


class User(mongodb.Document):
    # 账户
    username: str = mongodb.StringField(
        unique=True, min_length=8, max_length=20)
    # 密码
    password: str = mongodb.StringField(max_length=64)
    # 盐
    salt: str = mongodb.StringField(required=False)
    # 图片集
    photos: List[Photo] = mongodb.ListField(
        mongodb.ReferenceField(Photo))

    @staticmethod
    def encode_password(password: str, salt: str) -> str:
        """ 对密码进行md5编码 """
        magic_char = "token"
        s = password + magic_char + salt
        return encode_md5_from_string(s)

    @staticmethod
    def login(username: str, password: str) -> Tuple[bool, "User"]:
        """ 登录是否成功 """
        users: List[User] = User.objects(username=username)
        assert len(users) < 2, f"数据库异常, user: {username}, size: {len(users)}"
        user = users[0]
        s = User.encode_password(password, user.salt)
        return (s == user.password, user)

    @staticmethod
    def register(username: str, password: str) -> "User":
        """ 注册用户 """
        if not isinstance(username, str) or len(username) < 8 or not isinstance(password, str) or len(password) < 8:
            raise RequestError(Response.error(message="账户密码不能为空且均不可小于8位."))
        if User.is_exist_by_username(username):
            raise RequestError(f"改用户名已被注册")
        user = User(username=username, password=password)
        user.salt = random_string(8)
        user.password = User.encode_password(user.password, user.salt)
        user.photos = []
        user.save()
        return user

    @staticmethod
    def is_exist_by_username(username: str) -> bool:
        """用户名是否存在"""
        users = User.objects(username=username)
        size = len(users)
        is_exist = size == 1
        assert size <= 1, f"为何会有size: {size} 个 username: {username} 的用户?"
        return is_exist

    @staticmethod
    def query_by_id(id: str) -> Tuple["User", None]:
        """根据id查询用户"""
        users = User.objects(id=id)
        if users is None:
            return None
        return users[0]

    def get_id(self) -> str:
        return str(self.id)

    def add_photo(self, url: str):
        """增加图片"""
        if not isinstance(url, str):
            raise RequestError("增加图片数据异常")
        photo = Photo(original_url=url, userid=self.get_id())
        photo.save()
        self.photos.append(photo)
        self.update(push__photos=photo)

    def generate_token(self) -> Tuple[None, str]:
        token = {"id": self.get_id()}
        return encode_data(token)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "salt": self.salt,
            "photos": self.photos
        }

    def to_vo(self) -> Dict:
        """转换为vo数据, 避免泄漏加密信息"""
        return {
            "username": self.username,
            "photos": self.photos,
        }

    def __str__(self) -> str:
        return str(self.to_dict())


def test_user():
    from server.db.user import User
    from server.db.photo import Photo
    user = User.register("test", "test")
    user.photos.append(
        Photo(original_url="https://baidu.com", userid=user.get_id()))
    user.save()
