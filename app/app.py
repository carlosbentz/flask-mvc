from flask import Flask
from .views.views import register_views

app = Flask(__name__)

register_views(app)
