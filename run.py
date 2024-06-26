from flask import Flask, jsonify # Importar Flask y jsonify
from app.database import init_app # Importar la función init_app de app/database.py para inicializar la aplicación con la base de datos
#from app.views import index, saludar, prueba # Importar la función index de app/views.py
from app.views import * # Importar todas las funciones de app/views.py

# Crear una instancia de Flask para indicar que este archivo es el archivo principal
app = Flask(__name__) 

init_app(app) # Inicializar la aplicación con la base de datos

# Asociacion de las rutas '/' con la función index y el método al que se accede
app.route('/', methods=['GET'])(index)
app.route('/api/movies', methods=['GET'])(get_all_movies) # Asociar la ruta '/api/movies' con la función get_all_movies
app.route('/api/serch', methods=['GET'])(get_movie) # Asociar la ruta '/api/movies' con la función get_movie
app.route('/api/create', methods=['POST'])(create_movie) # Asociar la ruta '/api/movies' con la función create_movie
app.route('/api/update', methods=['PUT'])(update_movie) # Asociar la ruta '/api/movies' con la función update_movie
app.route('/api/delete', methods=['DELETE'])(delete_movie) # Asociar la ruta '/api/movies' con la función delete_movie

# Probar los métodos de la API

# Permite separar el código que se ejecuta cuando corre la aplicación
# 1. Ejecutar el archivo run.py (python run.py)
if __name__ == '__main__':
    app.run(debug=True) # Ejecutar la aplicación en modo debug para ver los errores

