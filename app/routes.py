from flask import flash, request, redirect, url_for, jsonify, render_template
from .models import db, mongo, UserMySQL
from sqlalchemy.sql import text
from bson.objectid import ObjectId 

def create_routes(app):
    @app.route('/create_mysql', methods=['POST'])
    def create_mysql():
        name = request.form['name']
        email = request.form['email']
        new_user = UserMySQL(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User created in MySQL', "mysql")
        return redirect(url_for('read_mysql_mongo'))

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
        flash('User created in MongoDB', "mongo")
        return redirect(url_for('read_mysql_mongo'))

    @app.route('/clear_mysql', methods=['POST'])
    def clear_mysql():
        try:
            # Eliminar todos los usuarios de la tabla MySQL
            UserMySQL.query.delete()
            db.session.commit()
            flash('MySQL database cleared', "mysql")
            return redirect(url_for('read_mysql_mongo'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}.', "mysql")
            return redirect(url_for('read_mysql_mongo'))

    @app.route('/delete_mysql', methods=['POST'])
    def delete_mysql_user():
        user_id = request.form.get('user_id')
        if user_id:
            user = db.session.query(UserMySQL).filter_by(id=int(user_id)).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                flash('Usuario eliminado exitosamente.', 'mysql')
            else:
                flash('Usuario no encontrado.', 'error')
        else:
            flash('ID de usuario no proporcionado.', 'mysql')
        return redirect(url_for('read_mysql_mongo'))

    @app.route('/update_mysql', methods=['POST'])
    def update_mysql_user():
        user_id = request.form.get('user_id')
        name = request.form['name']
        email = request.form['email']
        
        if user_id and name and email:
            user = db.session.query(UserMySQL).filter_by(id=int(user_id)).first()
            if user:
                user.name = name
                user.email = email 
                 
                db.session.commit()
                flash('Usuario actualizado exitosamente.', 'mysql')
            else:
                flash('Usuario no encontrado.', 'error')
        else:
            flash('Alguno de los campos no proporcionado.', 'mysql')
        return redirect(url_for('read_mysql_mongo'))
        
        
    @app.route('/delete_mongo', methods=['POST'])
    def delete_mongo_user():
        user_id = request.form.get('user_id')
        if user_id:
            try:
                object_id = ObjectId(user_id)

                # Delete the user document by ID
                result = mongo.db.users.delete_one({'_id': object_id})
                if result.deleted_count > 0:
                    flash('Usuario eliminado exitosamente.', 'mongo')
                else:
                    flash('Usuario no encontrado.', 'mongo')
            except Exception as e:
                flash(f'Error al eliminar el usuario: {e}', 'mongo')
        else:
            flash('ID de usuario no proporcionado.', 'mongo')
        return redirect(url_for('read_mysql_mongo'))

    @app.route('/update_mongo', methods=['POST'])
    def update_mongo_user():
        user_id = request.form.get('user_id')
        name = request.form['name']
        email = request.form['email']
        
        if user_id and name and email:
            try:
                object_id = ObjectId(user_id)
                # Update the user document by ID
                result = mongo.db.users.update_one(
                    {'_id': object_id},  # Filter by ID
                    {'$set': {'name': name, 'email': email}}  # Update fields
                )
                if result.modified_count > 0:
                    flash('Usuario actualizado exitosamente.', 'mongo')
                else:
                    flash('No se realizaron cambios en el usuario.', 'mongo')
            except Exception as e:
                flash(f'Error al actualizar el usuario: {e}', 'mongo')
        else:
            flash('Alguno de los campos no proporcionado.', 'mongo')
        return redirect(url_for('read_mysql_mongo'))
    
    @app.route('/clear_mongo', methods=['POST'])
    def clear_mongo():
        try:
            # Eliminar todos los documentos de la colección users en MongoDB
            mongo.db.users.delete_many({})
            flash('MongoDB database cleared', "mongo")
            return redirect(url_for('read_mysql_mongo'))
        except Exception as e:
            flash(f'Error: {str(e)}.', "mongo")
            return redirect(url_for('read_mysql_mongo'))