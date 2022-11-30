from . import mongodb


class User(mongodb.Document):
    username = mongodb.StringField(unique=True)
