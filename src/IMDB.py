import sys
from imdbpie import Imdb

def getMovieInfo(title):
    imdb = Imdb(anonymize = True)
    movie_id = imdb.search_for_title(title)[0]['imdb_id']
    movie = imdb.get_title_by_id(movie_id)
    movieInfo = ['Title: ' + movie.title, 'Rating: ' + str(movie.rating), 'Runtime: ' + str(int(movie.runtime)/60), 'Release Date: ' + movie.release_date, 'Certification: ' + movie.certification]
    return movieInfo
