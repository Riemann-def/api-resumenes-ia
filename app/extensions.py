from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from openai import OpenAI

db = SQLAlchemy()
mail = Mail()
openAi_client = OpenAI()