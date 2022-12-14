"""docs: http://docs.mongoengine.org/guide/defining-documents.html"""
from .package import *


class Global():
    def __init__(self):
        from flask_socketio import SocketIO
        from flask_mongoengine import MongoEngine
        from common.oss.manage import OssManage
        from .cache import Cache
        self.oss = OssManage()
        self.cache = Cache()
        self.socketio = SocketIO(async_mode='eventlet',cors_allowed_origins="*")
        self.mongodb = MongoEngine()


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


def get_socketio():
    """获得socketio"""
    return get_global().socketio


def get_mongodb():
    return get_global().mongodb
