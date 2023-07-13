from pydantic import BaseModel
import os
import sqlite3

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movies.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()



class Movie:
    def __init__(self, title, year, stars):
            self.title = title
            self.year = year
            self.stars = stars



    def create_table():
        # Crear tabla de películas
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                year INTEGER,
                stars REAL
            )
            """
        )
        #aplicar cambios
        conn.commit()

    @staticmethod
    def get_movies():
            c.execute("SELECT * FROM movies")
            rows = c.fetchall()
            movies = []
            for row in rows:
                movie = Movie(row[1], row[2], row[3])
                movies.append(movie)
                conn.close()
            return movies

    def save(self):
            c.execute("INSERT INTO movies (title, year, stars) VALUES (?,?,?)", (self.title, self.year, self.stars))
            conn.commit()
            conn.close()



