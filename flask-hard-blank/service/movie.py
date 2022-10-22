from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.director import DirectorService
from service.genre import GenreService


class MovieService:
    def __init__(self, dao: MovieDAO, genre_service: GenreService, director_service: DirectorService):
        self.dao = dao
        self.genre_service = genre_service
        self.director_service = director_service

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def create(self, data):
        movie = Movie(**data)

        movie.genre = self.genre_service.get_one(movie.id)
        movie.director = self.director_service.get_one(movie.id)

        return self.dao.create(movie)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        movie.genre = self.genre_service.get_one((movie.id))
        movie.director = self.director_service.get_one(movie.id)

        return self.dao.update(movie)