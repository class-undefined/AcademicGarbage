import random
import string
import hashlib
from itsdangerous import TimedJSONWebSignatureSerializer
from typing import Any, Union
from server.app import app

GLOBAL_SALT = app.config.get("AUTO_SALT")  # 随机盐
GLOBAL_SECRET_KEY = app.config.get("AUTO_SECRET_KEY")
STRING_SEED = string.ascii_letters + string.digits
serializer = TimedJSONWebSignatureSerializer(
    GLOBAL_SECRET_KEY, salt=GLOBAL_SALT)


def random_string(size: int) -> str:
    """生成指定size长度的随机字符串 范围: a-zA-Z0-9"""
    return "".join(random.sample(STRING_SEED, size))


def encode_md5_from_string(s: str) -> str:
    """md5编码"""
    return hashlib.md5(s.encode("utf8")).hexdigest()


def encode_data(data: Any) -> Union[str, bytes]:
    """数据编码"""
    return serializer.dumps(data)


def decode_data(s: Union[str, bytes]) -> Any:
    """数据解码"""
    return serializer.loads(s)
