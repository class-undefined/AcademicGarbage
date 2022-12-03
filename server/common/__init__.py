from .package import *


class Global():
    def __init__(self):
        from common.oss.manage import OssManage
        from .cache import Cache
        self.oss = OssManage()
        self.cache = Cache()


__gloabl = Global()


def get_global():
    """获得全局对象"""
    return __gloabl


def get_oss():
    """获得oss"""
    return get_global().oss


def get_cache():
    """获得缓存"""
    return get_global().cache
