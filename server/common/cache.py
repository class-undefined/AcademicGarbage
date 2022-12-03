import json
from typing import TYPE_CHECKING, Union, Dict, List
from .package import get_variable_type
if TYPE_CHECKING:
    import redis

Value = Union[str, int, float, Dict, List]


class Cache():
    def __init__(self):
        self.redis = Cache.__create_redis()
        self.types = ['bool', 'str', 'int',
                      'str', 'float', 'list', 'dict', 'NoneType']  # 支持存储的类型

    @staticmethod
    def __create_redis() -> "redis.Redis":
        """创建redis实例"""
        from app import app
        from redis import Redis
        config = app.config
        host = config["REDIS_HOST"]
        port = config["REDIS_PORT"]
        db = config["REDIS_DB"]
        return Redis(host=host, port=port, db=db, decode_responses=True)

    def __check_variable_type_in_whitelist(self, val: Value) -> bool:
        """检查变量是否在白名单内"""
        typeof = get_variable_type(val)
        assert typeof in self.types, f"{typeof}类型不在白名单: {self.types}中"

    def __wrap_variable(val: Value) -> str:
        """数据包装"""
        typeof = get_variable_type(val)
        pair = [typeof, val]
        return json.dumps(pair)

    def __unwrap_variable_value(self, s: Union[str, None]) -> Value:
        """数据解包"""
        if s is None:
            return None
        pair = json.loads(s)
        # 就目前而言, 如果是基本类型, 那么json已自动转换了数据类型, 所以暂时无需手写转换
        return pair[0]

    def put(self, key: str, val: Value, expires_in: Union[float, None] = None):
        """
        存放数据
        @key: 键
        @val: 值
        @expires_in: 键过期时间 默认不过期 单位: 秒
        """
        self.__check_variable_type_in_whitelist(val)
        pair = self.__wrap_variable(val)
        self.redis.set(key, pair, ex=expires_in)

    def pull(self, key: str) -> Value:
        s = self.redis.get(key)
        pair = self.__unwrap_variable_value(s)
        return pair[1]
