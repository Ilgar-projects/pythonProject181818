from dao.movie import MovieDAO
from dao.genre import GenreDAO
from setup_db import db
from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService
from service.director import DirectorDAO


movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)

genre_service = GenreService(genre_dao)

director_service = DirectorService(director_dao)

movie_service = MovieService(movie_dao, genre_service, director_service)
