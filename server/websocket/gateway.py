from common.package import debug
from websocket import socketio
from flask import request


@socketio.on("connect", namespace="/")
def connected():
    debug(request.sid)
    socketio.emit("message", "ok", room=request.sid)
