from typing import Dict
from server.db.user import User
from server.services.auth import decode_data


def user_parser(headers: Dict):
    """ 解析user token信息 """
    # token_data = decode_data(headers['Token'])
    # assert isinstance(token_data, dict), "错误的token"
    assert "Token" in headers, "header中无Token字段"
    user_id = headers['Token']  # token_data['id']
    assert user_id is not None, "token中无id属性"
    users = User.objects(id=user_id)
    assert len(users) == 1, f"id异常, id: {user_id}, 包含多个用户"
    user = users[0]
    return user
