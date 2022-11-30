import random
import string
import hashlib
STRING_SEED = string.ascii_letters + string.digits


def random_string(size: int) -> str:
    """生成指定size长度的随机字符串 范围: a-zA-Z0-9"""
    return "".join(random.sample(STRING_SEED, size))


def encode_md5_from_string(s: str) -> str:
    """md5编码"""
    return hashlib.md5(s.encode("utf8")).hexdigest()
