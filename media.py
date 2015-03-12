#!/usr/bin/env python

import webbrowser

class Movie():
    
    valid_ratings = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_plot, poster_image, youtube_trailer):
        self.title = movie_title
        self.plot = movie_plot
        self.poster_image_url = poster_image
        self.youtube_trailer_url = youtube_trailer
        
    def show_trailer(self):
        # opens the youtube trailer url in browser window
        webbrowser.open(self.youtube_trailer_url)
        