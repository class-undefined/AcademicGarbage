import functools
from flask import request
from common.error import RequestError
from common.package import decode_data, encode_data
from common.response import Response
from services.parsers import user_parser


def interceptor():
    """ 异常拦截器, 异常自动包装成Response, 返回Response则调用to_response """
    def handle(route_func):
        @functools.wraps(route_func)
        def wrapper(*args, **kwargs):
            try:
                rst = route_func(*args, **kwargs)
                # 如果返回的是Response, 则无需手动调用to_response
                if isinstance(rst, Response):
                    return rst.to_response()
                return route_func(*args, **kwargs)
            except RequestError as e:
                return e.response.to_response()
        return wrapper
    return handle
    