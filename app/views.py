from flask import render_template
from app import app
from .request import get_movies, get_movie

#Views
@app.route('/')
def index():
    '''
    View root page function that returns index page and it's data
    '''

    #Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = "Home - Welcome to the best Movie Review Website Online"
    message = "Hello World!!!!"
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie = movie)