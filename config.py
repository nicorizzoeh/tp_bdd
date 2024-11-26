class Config:
    # Configuración MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración MongoDB
    MONGO_URI = "mongodb://localhost:27017/testdb"


