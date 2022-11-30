from .app import app
from .db import register_db
from .db.user import User, test_user
from .db.photo import Photo
from .controller.export import user_blue
register_db(app)


@app.route("/")
def hello():
    # test_user()
    return "done"


app.register_blueprint(user_blue)
