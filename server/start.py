from flask_socketio import SocketIO
from app import app
from db.user import User, test_user
from controller.export import user_blue
from common import get_socketio, get_mongodb
from db.photo import Photo
from websocket import gateway
app.config['SECRET_KEY'] = 'secret!'
get_socketio().init_app(app)
get_mongodb().init_app(app)
app.register_blueprint(user_blue)


@app.route("/")
def hello():
    # test_user()
    return "done"


if __name__ == "__main__":
    get_socketio().run(app, host=app.config["HOST"], port=app.config["PORT"])
