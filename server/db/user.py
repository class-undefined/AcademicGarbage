from typing import List, Tuple
from server.db import mongodb
from server.db.photo import Photo
from server.common.package import random_string, encode_md5_from_string
# from mongoengine import StringField


class User(mongodb.Document):
    # 账户
    username = mongodb.StringField(unique=True, max_length=20)
    # 密码
    password = mongodb.StringField(max_length=64)
    # 盐
    salt = mongodb.StringField(required=False)
    # 图片集
    photos = mongodb.ListField(mongodb.EmbeddedDocumentField(Photo))

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
        user = User(username=username, password=password)
        user.salt = random_string(8)
        user.password = User.encode_password(user.password, user.salt)
        user.photos = []
        user.save()
        return user


def test_user():
    from server.db.user import User
    from server.db.photo import Photo
    user = User.register("test", "test")
    user.photos.append(Photo(original_url="https://baidu.com"))
    user.save()
