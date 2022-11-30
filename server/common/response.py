from typing import Dict, Union
from flask import make_response, jsonify


class Response():
    """ Http Response """

    def __init__(self, data: Dict=None, message: Union[str, None] = None, code: int = 0):
        self.response = {"data": data, "message": message, "code": code}

    def __update(self, data: Dict=None, message: Union[str, None] = None, code: int = 0):
        self.response = {"data": data, "message": message, "code": code}

    def ok(self, data: Dict=None, message: Union[str, None] = "操作成功"):
        """操作成功"""
        self.__update(data, message, 20000)
        return make_response(jsonify(self.response))

    def error(self, data: Dict=None, message: Union[str, None] = "操作失败"):
        """操作失败"""
        self.__update(data, message, 20001)
        return make_response(jsonify(self.response))

    def relogin(self):
        """重新登录"""
        self.__update(None, "登录失败, 请重新登录", 30001)
        return make_response(jsonify(self.response))