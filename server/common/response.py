from typing import Dict, Union
from flask import make_response, jsonify


class Response():
    """ Http Response """

    def __init__(self, message: Union[str, None] = None, data: Dict = None,  code: int = 0):
        self.__response = {"data": data, "message": message, "code": code}

    @staticmethod
    def ok(message: Union[str, None] = "操作成功", data: Dict = None, ) -> "Response":
        """操作成功"""
        return Response(data=data, message=message, code=20000)

    @staticmethod
    def error(message: Union[str, None] = "操作失败", data: Dict = None, ) -> "Response":
        """操作失败"""
        return Response(data=data, message=message, code=20001)

    def to_response(self):
        """转换为ResponseBody"""
        return make_response(jsonify(self.__response))

    def to_dict(self) -> Dict:
        return self.__response

    @staticmethod
    def relogin() -> "Response":
        """重新登录"""
        return Response(None, "登录失败, 请重新登录", 30001)
