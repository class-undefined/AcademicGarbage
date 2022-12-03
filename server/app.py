from flask import Flask
from settings import EnvConfig
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config.from_object(EnvConfig)
