from flask import Flask
from flask_mongoengine import MongoEngine
"""docs: http://docs.mongoengine.org/guide/defining-documents.html"""
mongodb = MongoEngine()


def register_db(app: "Flask"):
    """注册db"""
    mongodb.init_app(app, app.config)
