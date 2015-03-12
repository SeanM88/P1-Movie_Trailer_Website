#!/usr/bin/env python

import media
import fresh_tomatoes

# Create movie objects
pacific_rim = media.Movie("Pacific Rim",
                        "Robots fight aliens",
                        "http://content7.flixster.com/movie/11/17/39/11173933_800.jpg",
                        "http://www.youtube.com/watch?v=2vKz7WnU83E")

the_dark_knight = media.Movie("The Dark Knight",
                     "The sequel to Batman Begins.",
                     "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX640_SY720_.jpg",
                     "http://www.youtube.com/watch?v=GROmJWb-3wU")

fight_club = media.Movie("Fight Club",
                         "A movie about more than fighting",
                         "http://images.moviepostershop.com/fight-club-movie-poster-1999-1020215604.jpg",
                         "http://www.youtube.com/watch?v=SUXWAEX2jlg")

movies = [pacific_rim, the_dark_knight, fight_club]

fresh_tomatoes.open_movies_page(movies) 