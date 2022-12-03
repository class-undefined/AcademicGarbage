from flask import Flask
from settings import EnvConfig
app = Flask(__name__)
app.config.from_object(EnvConfig)
