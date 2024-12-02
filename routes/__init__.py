from flask import Blueprint
from routes.summary import summary_bp

def register_blueprints(app):
    app.register_blueprint(summary_bp)
