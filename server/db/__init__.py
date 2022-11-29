from flask_pymongo import PyMongo
from flask import Flask
from .config import *
__db = PyMongo()


def register_db(app: "Flask"):
    """注册db"""
    __db.init_app(app, uri=URI)


def get_db() -> PyMongo:
    """获取db"""
    return __db
