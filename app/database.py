import os
import mysql.connector
from flask import g # Importar la variable g de Flask para almacenar la conexión a la base de datos
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear una función para obtener la conexión a la base de datos

DATABASE_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'), # Carga los datos desde el archivo .env donde está almacenada la clave
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT',3300)
}

# Crear una función para obtener la conexión a la base de datos
# Función para obtener la conexión a la base de datos
def get_db():
    # Si 'db' no está en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear una nueva conexión a la base de datos y guardarla en 'g'
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    # Retornar la conexión a la base de dato
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)  # Eliminar la conexión a la base de datos
    # Si la conexión existe, cerrarla
    if db is not None:
        db.close()
    # Devolver la conexión a la base de datos
    return g.db

# Función para inicializar la aplicación con el manejo de la base de datos y luego cerrar la conexión
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)
                          