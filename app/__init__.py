from flask import Flask
from .config import DevConfig

#Initialize application
app = Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)

from app import views