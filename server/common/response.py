from typing import Dict, Union
from flask import make_response, jsonify


class Response():
    """ Http Response """

    def __init__(self, data: Dict = None, message: Union[str, None] = None, code: int = 0):
        self.__response = {"data": data, "message": message, "code": code}

    def diy(self, data: Dict = None, message: Union[str, None] = None, code: int = 0) -> "Response":
        """自定义Response"""
        self.__response = {"data": data, "message": message, "code": code}
        return self

    def ok(self, data: Dict = None, message: Union[str, None] = "操作成功"):
        """操作成功"""
        return self.diy(data, message, 20000).to_response()

    def error(self, data: Dict = None, message: Union[str, None] = "操作失败"):
        """操作失败"""
        return self.diy(data, message, 20001).to_response()

    def to_response(self):
        """转换为ResponseBody"""
        return make_response(jsonify(self.__response))

    def to_dict(self) -> Dict:
        return self.__response

    @staticmethod
    def relogin():
        """重新登录"""
        response = Response(None, "登录失败, 请重新登录", 30001)
        return make_response(jsonify(response.to_dict()))
