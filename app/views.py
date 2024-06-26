from flask import jsonify
from app.models import Movie

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de las peliculas
def get_all_movies():
    movies = Movie.get_all()
    list_movies = [movie.serialize() for movie in movies] # Serializar los objetos de la clase Movie
    return jsonify(list_movies)

#funcion que busca una pelicula
def get_movie():
    pass

# Función para crear una nueva película
def create_movie():
    pass

# Función para actualizar una película
def update_movie():
    pass

# Función para eliminar una película
def delete_movie():
    pass