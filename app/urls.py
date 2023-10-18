from flask import Blueprint
from app.handlers import index, login, register, new_chat, chat

app_routes = Blueprint("app_routes", __name__)

app_routes.add_url_rule('/', 'index', index, methods=["POST", "GET"])
app_routes.add_url_rule('/login', 'login', login, methods=["POST", "GET"])
app_routes.add_url_rule('/register', 'register', register, methods=["POST", "GET"])
app_routes.add_url_rule('/new-chat', 'new_chat', new_chat, methods=["POST"])
app_routes.add_url_rule('/chat/', 'chat', chat)