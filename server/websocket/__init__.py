from flask_socketio import SocketIO
from flask import Flask
socketio = SocketIO(async_mode='eventlet')


def register_socketio(app: "Flask"):
    """注册socketio"""
    socketio.init_app(app)
