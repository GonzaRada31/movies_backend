from app.database import get_db

class Movie:
    #CONSTRUCTOR - Agregamos valores por defecto para que no sea obligatorio enviar todos los valores  
    def __init__(self,id_movie=None,title=None,director=None,release_date=None,banner=None):
        self.id_movie = id_movie
        self.title = title
        self.director = director
        self.release_date = release_date
        self.banner = banner

    # Decorador de método es estático, significa que no necesita una instancia de la clase para ser llamado
    @staticmethod    
    def get_all():
        db = get_db() # Obtener la conexión a la base de datos
        cursor = db.cursor() # es una instancia de la clase cursor que permite ejecutar sentencias SQL
        cursor.execute('SELECT * FROM movie')    
        rows = cursor.fetchall() # Devuelve una lista de tuplas con los registros de la tabla
        # Crear una lista de objetos de la clase Movie porque el cursor.fetchall() devuelve una lista de tuplas
        movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4]) for row in rows]
        cursor.close() # Cerrar el cursor    
        pass

    def save(self):
        #logica para INSERT/UPDATE en base datos
        pass

    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass

    def serialize(self):
        return {
            'id_movie': self.id_movie,
            'title': self.title,
            'director': self.director,
            'release_date': self.release_date,
            'banner': self.banner,
        }
    
    