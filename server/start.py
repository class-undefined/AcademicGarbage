from .app import app
from .db import register_db
from .controller.export import user_blue
register_db(app)


@app.route("/")
def hello():
    return "done"


app.register_blueprint(user_blue)
