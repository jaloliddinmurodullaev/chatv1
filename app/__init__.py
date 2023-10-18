import os
from flask import (
    Flask
)
from flask_socketio import SocketIO
from faunadb.client import FaunaClient
from dotenv import load_dotenv

load_dotenv()

# Initialize client connection to database
client = FaunaClient(secret=os.getenv("FAUNA_KEY"))

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Initialize socketio application
socketio = SocketIO(app)

from app.urls import app_routes

app.register_blueprint(app_routes)