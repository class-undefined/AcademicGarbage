from typing import List, Tuple, Dict, Any
from common.error import RequestError
from common.response import Response
from db import mongodb
from db.photo import Photo
from common.package import encode_data, random_string, encode_md5_from_string
from common import get_socketio, get_cache, debug
import datetime

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
        if len(users) == 0:
            raise RequestError("账号或密码错误") 
        user = users[0]
        s = User.encode_password(password, user.salt)
        return (s == user.password, user)

    @staticmethod
    def register(username: str, password: str) -> "User":
        """ 注册用户 """
        if not isinstance(username, str) or len(username) < 8 or not isinstance(password, str) or len(password) < 8:
            raise RequestError(Response.error(message="账户密码不能为空且均不可小于8位."))
        if User.is_exist_by_username(username):
            raise RequestError(f"该用户名已被注册")
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

    def add_photo(self, url: str) -> "Photo":
        """增加图片"""
        if not isinstance(url, str):
            raise RequestError("增加图片数据异常")
        photo = Photo(original_url=url, userid=self.get_id())
        try:
            photo.save()
        except Exception as e:
            debug(e)
            raise RequestError("保存图片失败")
        self.photos.append(photo)
        self.update(push__photos=photo)
        return photo

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
        photos = []
        for photo in self.photos:
            photos.append(photo.to_dict())
        return {
            "username": self.username,
            "photos": photos,
        }

    def send_msg(self, val: Any):
        """发送socket消息"""
        cache = get_cache()
        sid = cache.pull(group="user", key=self.get_id())
        if sid is None: # 如果没有sid, 说明已过期, 不进行发送
            return
        get_socketio().emit("message", val, room=sid)

    def query_by_create_range(self, start_date: datetime.date, end_date: datetime.date):
        """查询指定日期范围创建的图片"""
        photos = self.photos
        rst: List["Photo"] = []
        for photo in photos:
            if photo.create_time >= start_date and photo.create_time <= end_date:
                rst.append(photo)
        return rst


    def get_create_photos_by_today(self):
        """查询今天创建的图片"""
        today = datetime.date.today()
        start_date = datetime.datetime.combine(today, datetime.time.min)
        end_date = datetime.datetime.combine(today, datetime.time.max)
        return self.query_by_create_range(start_date, end_date)

    def get_photos(self) -> List["Photo"]:
        """获取所有图片"""
        return self.photos


    def __str__(self) -> str:
        return str(self.to_dict())


def test_user():
    from server.db.user import User
    from server.db.photo import Photo
    user = User.register("test", "test")
    user.photos.append(
        Photo(original_url="https://baidu.com", userid=user.get_id()))
    user.save()
