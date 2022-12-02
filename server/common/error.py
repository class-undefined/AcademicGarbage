from server.common.response import Response


class RequestError(Exception):  # 请求异常
    def __init__(self, code=20001, message="请求错误", data=None):
        self.response = Response(code=code, message=message, data=data)

    @staticmethod
    def from_response(response: Response) -> "RequestError":
        params = response.to_dict()
        return RequestError(**params)


def test():
    """验证请求拦截"""
    response = Response.error()
    try:
        raise RequestError.from_response(response)
    except RequestError as e:
        response = e.response.to_dict()
        assert response == {'data': None, 'message': '操作失败', 'code': 20001}
