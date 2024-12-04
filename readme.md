# Trabajo Practico Final BDD

## Integrantes

 * Agustin Braida, Padrón: 106301
 * Mateo Bulnes, Padrón: 106211
 * Nicolas Agustin Rizzo Ehrenbock, Padrón: 109756
 * Franco Favotti, Padrón: 109388
 * Franco Gentilini, Padrón: 108733
 * Martín Saad, Padrón: 110171


## Como usar

Para instalar las dependencias

```
    pip install -r requeriments.txt
```

La app se comunica con la bdd no relacional a traves del puerto especificado en la variable de configuracion MONGO_URI (por defecto 27017). Ejemplo de como levantar la bdd en docker:

```
    export MONGODB_VERSION=6.0-ubi8
    docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server:$MONGODB_VERSION
```

Para correr la aplicacion
    
```
    python3 run.py
```
