import functools
from flask import request
from common.package import decode_data, encode_data
from services.parsers import user_parser


def auth_guard(token_parser=user_parser):
    """ 通用验证守卫 """
    def handle(route_func):
        @functools.wraps(route_func)
        def wrapper(*args, **kwargs):
            data = token_parser(dict(request.headers))
            return route_func(*args, data=data, **kwargs)
        return wrapper
    return handle


def user_auth_guard(route_func):
    """用户验证守卫, 会读取header的Token字段, 若存在数据会尝试解析, 若成功登录则在路由函数参数中拥有data字段, 即为User"""
    handler = auth_guard(token_parser=user_parser)
    return handler(route_func)


def test_encode_decode():
    """单元测试-测试编码解码"""
    datas = ['123', 123, True, {"a": True}, ['good', 2]]
    secret = encode_data(datas)
    rst = decode_data(secret)
    assert rst == datas
