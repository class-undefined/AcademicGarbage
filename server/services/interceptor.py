import functools
from flask import request
from server.common.error import RequestError
from server.common.package import decode_data, encode_data
from server.services.parsers import user_parser


def interceptor():
    """ 异常拦截器 """
    def handle(route_func):
        @functools.wraps(route_func)
        def wrapper(*args, **kwargs):
            try:
                return route_func(*args, **kwargs)
            except RequestError as e:
                return e.response.to_response()
        return wrapper
    return handle
    