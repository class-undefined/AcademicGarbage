from flask import Blueprint

user_blue = Blueprint("user", __name__, url_prefix="/user")


@user_blue.route("/register")
def register():
    return "register"


@user_blue.route("/login")
def login():
    return "login"

@user_blue.route("/history")
def history():
    return "history"