from typing import Dict
from common.package import debug
from db.user import User
from services.auth import decode_data

def user_parser(headers: Dict):
    """ 解析user token信息, 若解析失败返回None """
    # assert isinstance(token_data, dict), "错误的token"
    if "Token" not in headers:
        debug("header中无Token字段")
        return None
    token_data = decode_data(headers['Token'])  # token_data['id']
    if not isinstance(token_data, dict):
        debug("错误的token")
        return None
    user_id = token_data['id']
    if user_id is None:
        debug("token中无id属性")
        return None
    users = User.objects(id=user_id)
    assert len(users) == 1, f"id异常, id: {user_id}, 包含多个用户"
    user = users[0]
    return user
