from flask import Flask
from .models import db, mongo
from .routes import create_routes

def create_app():
    app = Flask(__name__, template_folder='templates/')
    app.config.from_object('config.Config')
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db.init_app(app)
    mongo.init_app(app)

    # Registrar rutas después de crear la aplicación
    create_routes(app)

    return app