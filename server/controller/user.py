from typing import Dict
from flask import Blueprint

from server.services.auth import user_auth_guard

user_blue = Blueprint("user", __name__, url_prefix="/user")


@user_blue.route("/register")
def register():
    return "register"


@user_blue.route("/login", methods=["POST"])
@user_auth_guard
def login(data: Dict):
    print(data)
    return "login"


@user_blue.route("/history")
def history():
    return "history"
