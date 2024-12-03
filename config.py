import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configuración MySQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración MongoDB
    MONGO_URI = "mongodb://localhost:27017/testdb"


