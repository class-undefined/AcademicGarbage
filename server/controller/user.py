from typing import Dict, Union
from flask import Blueprint, request
from server.common.error import RequestError
from server.common.response import Response
from server.db.user import User

from server.services.auth import user_auth_guard
from server.services.interceptor import interceptor

user_blue = Blueprint("user", __name__, url_prefix="/user")


@user_blue.route("/register", methods=["POST"])
@interceptor()
def register():
    body = request.get_json()
    if "username" not in body or "password" not in body:
        return Response().error(message="缺少账户或密码!")
    user = User.register(**body)
    return Response.ok(message="注册成功", data=user.to_vo())


@user_blue.route("/login", methods=["POST"])
@user_auth_guard
@interceptor()
def login(data: Union[User, None]):
    body = request.get_json()
    response_data = {
        "token": None,
        "user": None
    }
    # body为空且token验证失败, 需要重新登录
    if body is None and data is None:
        return Response.relogin()
    # 用登录参数优先验证登录参数
    if body is not None:
        if "username" not in body or "password" not in body:
            return Response().error(message="账户或密码错误!")
        username = body["username"]
        password = body["password"]
        is_login, user = User.login(username=username, password=password)
        if is_login:
            response_data["user"] = user.to_vo()
            response_data["token"] = user.generate_token()
            return Response().ok(data=response_data, message="登录成功")
        raise RequestError("账户或密码错误")
    # token验证成功, 返回用户
    if data is not None:
        response_data["user"] = data.to_vo()
        return Response().ok(data=response_data, message="登录成功")
    # 否则重新登录
    return Response.relogin()


@user_blue.route("/history", methods=["GET"])
@user_auth_guard
@interceptor()
def history(data: Union[User, None]):
    if data is None:
        return Response.relogin()
    # 暂不考虑分页
    photos = []
    for photo in data.photos:
        photos.append(photo.to_dict())
    return Response.ok(data=photos)


@user_blue.route("/add_photo", methods=["POST"])
@user_auth_guard
@interceptor()
def add_photo(data: Union[User, None]):
    user = data
    body = request.get_json()
    if user is None:
        return Response.relogin()
    user.add_photo(body["url"])
    return Response.ok()
