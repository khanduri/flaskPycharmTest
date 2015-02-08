from flask import Flask


app = Flask(__name__)


from app.compute import api
from app.compute import routes


__all__ = [
    'app',
]