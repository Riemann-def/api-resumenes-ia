from flask_mail import Message
from app.extensions import mail

def send_summary_email(email, url, summary):
    msg = Message(
        subject="Tu resumen generado",
        recipients=[email],
        body=f"¡Hola!\n\nAquí tienes el resumen solicitado de la noticia:\n\nCategoría: {summary['category']}\nTono: {summary['tone']}\nNivel de fake news: {summary['fake_news_level']}\n\nPuedes leer el artículo completo aquí: {url}\n\n¡Esperamos que te sea útil!"
    )
    mail.send(msg)
