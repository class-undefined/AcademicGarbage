from itsdangerous import URLSafeSerializer
from server.common.package import random_string
from typing import Any, Union
from server.app import app
GLOBAL_SALT = app.config.get("AUTO_SALT")  # 随机盐
GLOBAL_SECRET_KEY = app.config.get("AUTO_SECRET_KEY")
serializer = URLSafeSerializer(GLOBAL_SECRET_KEY, salt=GLOBAL_SALT)


def encode_data(data: Any) -> Union[str, bytes]:
    """数据编码"""
    return serializer.dumps(data)


def decode_data(s: Union[str, bytes]) -> Any:
    """数据解码"""
    return serializer.loads(s)


def test_encode_decode():
    """单元测试-测试编码解码"""
    datas = ['123', 123, True, {"a": True}, ['good', 2]]
    secret = encode_data(datas)
    rst = decode_data(secret)
    assert rst == datas
