from flask import Flask
from flask_cors import CORS  # Importar CORS
from app.config import Config
from app.extensions import db, mail
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS
    CORS(app)

    # Inicializar extensiones
    db.init_app(app)
    mail.init_app(app)

    # Registrar rutas
    register_blueprints(app)

    return app
