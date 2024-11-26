from flask import Flask, request, jsonify, render_template
from .models import db, mongo, UserMySQL

def create_routes(app):
    @app.route('/create_mysql', methods=['POST'])
    def create_mysql():
        name = request.form['name']
        email = request.form['email']
        new_user = UserMySQL(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created in MySQL"})

    @app.route('/', methods=['GET'])
    def read_mysql_mongo():
        # Obtener usuarios de MySQL
        mysql_users = UserMySQL.query.all()

        # Obtener usuarios de MongoDB
        mongo_users = mongo.db.users.find()
        
        # Convertir el cursor de MongoDB en una lista
        mongo_users_list = list(mongo_users)
        
        # Pasar ambos conjuntos de usuarios a la plantilla
        return render_template('index.html', users=mysql_users, mongo_users=mongo_users_list)

    @app.route('/create_mongo', methods=['POST'])
    def create_mongo():
        name = request.form['name']
        email = request.form['email']
        user_data = {'name': name, 'email': email}
        mongo.db.users.insert_one(user_data)
        return jsonify({"message": "User created in MongoDB"})

    @app.route('/clear_mysql', methods=['POST'])
    def clear_mysql():
        try:
            # Eliminar todos los usuarios de la tabla MySQL
            UserMySQL.query.delete()
            db.session.commit()
            return jsonify({"message": "MySQL database cleared!"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": f"Error: {str(e)}"}), 500

    @app.route('/clear_mongo', methods=['POST'])
    def clear_mongo():
        try:
            # Eliminar todos los documentos de la colección users en MongoDB
            mongo.db.users.delete_many({})
            return jsonify({"message": "MongoDB database cleared!"}), 200
        except Exception as e:
            return jsonify({"message": f"Error: {str(e)}"}), 500