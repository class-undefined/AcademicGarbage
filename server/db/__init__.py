from flask import Flask
from flask_mongoengine import MongoEngine
mongodb = MongoEngine()


def register_db(app: "Flask"):
    """注册db"""
    print(app.config)
    mongodb.init_app(app, app.config)


# def get_db() -> PyMongo:
#     """获取db"""
#     return __db
