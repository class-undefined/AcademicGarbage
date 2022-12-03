from flask_socketio import SocketIO
from app import app
from db import register_db
from db.user import User, test_user
from db.photo import Photo
from controller.export import user_blue
from websocket import register_socketio, socketio, gateway
app.config['SECRET_KEY'] = 'secret!'
register_db(app)
register_socketio(app)
app.register_blueprint(user_blue)


@app.route("/")
def hello():
    # test_user()
    return "done"


if __name__ == "__main__":
    socketio.run(app, host=app.config["HOST"], port=app.config["PORT"])
