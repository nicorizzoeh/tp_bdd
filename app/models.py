from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

# Inicializa las extensiones
db = SQLAlchemy()
mongo = PyMongo()

# Modelo Relacional (MySQL)
class UserMySQL(db.Model):
    __tablename__ = 'user_my_sql'  # Especifica el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Modelo NoSQL (MongoDB)
class UserMongo:
    def __init__(self, name, email):
        self.name = name
        self.email = email