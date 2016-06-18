import sys
from imdbpie import Imdb

def main():

    title = sys.argv[-1]
    
    imdb = Imdb()

    movie = imdb.get_title_by_id(imdb.search_for_title(title)[0]['imdb_id'])

    movie_list = [movie.title, movie.rating, str(int(movie.runtime)/60), movie.release_date, movie.certification]

    print(str(movie_list))

main()
