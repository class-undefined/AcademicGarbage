from itsdangerous import URLSafeSerializer
from server.common.package import random_string
from typing import Any, Union
from server.app import app
GLOBAL_SALT = app.config.get("AUTO_SALT")  # 随机盐
GLOBAL_SECRET_KEY = app.config.get("AUTO_SECRET_KEY")
serializer = URLSafeSerializer(GLOBAL_SECRET_KEY, salt=GLOBAL_SALT)


def encode_data(data: Any) -> Union[str, bytes]:
    return serializer.dumps(data)


def decode_data(s: Union[str, bytes]) -> Any:
    return serializer.loads(s)


def test_decode():
    datas = ['123', 123, True, {"a": True}, ['good', 2]]
    secret = encode_data(datas)
    rst = decode_data(secret)
    assert rst == datas
