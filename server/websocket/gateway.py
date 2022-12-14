from common.package import debug, decode_data
from common import get_cache, get_socketio
from flask import request
socketio = get_socketio()
namespace = "/"


@socketio.on("connect", namespace=namespace)
def connected():
    socketio.emit("connected", "ok", room=request.sid)


@socketio.on("bind", namespace=namespace)
def bind(token: str):
    """绑定客户端, 将sid缓存至redis"""
    token_data = decode_data(token)
    user_id = token_data['id']
    cache = get_cache()
    sid = request.sid
    cache.put(group="user", key=user_id, val=sid,
              expires_in=60 * 60 * 24)  # 一天过期
    socketio.emit("binded", "ok")
