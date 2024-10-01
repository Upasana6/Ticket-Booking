from movie import Movie


class MovieController:
    movies_map: dict[str, list[Movie]]
    all_movies: list[Movie]

    def __init__(self, city_to_movie: dict[str, list[Movie]], all_movies: list[Movie]) -> None:
        self.movies_map = city_to_movie
        self.all_movies = all_movies
