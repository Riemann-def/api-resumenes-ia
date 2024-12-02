import enum
from app.extensions import db
from models.base import BaseModel

class Summary(BaseModel):
    original_url = db.Column(db.String(500), nullable=False)
    summary_text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # Categoría de la noticia
    tone = db.Column(db.String(50), nullable=False)          # Tono de la noticia
    fake_news_level = db.Column(db.String(50), default='Ninguno')  # Nivel de fake news
