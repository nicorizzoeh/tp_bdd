from app import create_app, db

app = create_app()

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()  # Esto c

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)