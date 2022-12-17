import random
import string
import hashlib
import inspect
import re
from typing import Any, Union
from app import app
from authlib.jose import jwt
import time

GLOBAL_SALT = app.config.get("AUTO_SALT")  # 随机盐
GLOBAL_SECRET_KEY = app.config.get("AUTO_SECRET_KEY")
AUTO_TOKEN_EXPIRES_IN = app.config.get("AUTO_TOKEN_EXPIRES_IN")  # token 过期时间
STRING_SEED = string.ascii_letters + string.digits


def random_string(size: int) -> str:
    """生成指定size长度的随机字符串 范围: a-zA-Z0-9"""
    return "".join(random.sample(STRING_SEED, size))


def encode_md5_from_string(s: str) -> str:
    """md5编码"""
    return hashlib.md5(s.encode("utf8")).hexdigest()


def encode_data(data: dict, exp_seconds: int = AUTO_TOKEN_EXPIRES_IN) -> str:
    """数据编码"""
    # 签名算法
    header = {'alg': 'HS256', "typ": "JWT"}
    # 用于签名的密钥
    key = GLOBAL_SECRET_KEY
    exp = int(time.time()) + exp_seconds
    payload = {"exp": exp}
    payload.update(data)
    # 待签名的数据负载
    return jwt.encode(header=header, payload=data, key=key).decode("utf8")


def decode_data(s: str) -> dict:
    """数据解码"""
    payload = None
    try:
        payload = jwt.decode(s, GLOBAL_SECRET_KEY)
    except Exception as e:
        debug(e)
        pass
    if payload is None:
        return None
    if "exp" in payload:
        exp = payload["exp"]
        if time.time() > exp:
            return None
            # raise Exception("Token expired")
    return payload


def debug(*args, back=1):
    frame = inspect.currentframe()
    while back:
        frame = frame.f_back
        back -= 1
    co = frame.f_code
    filename = co.co_filename
    prefix = f"{filename}:{frame.f_lineno} "
    print(f"{prefix:40}", *args, flush=True)


def get_variable_type(val: Any) -> str:
    """获得变量类型字符串"""
    regex = r"<class '(.*)'>"
    typeof = str(type(val))
    matches = re.findall(regex, typeof, re.MULTILINE)
    assert len(matches) == 1, "不支持重写类型"
    return matches[0]
