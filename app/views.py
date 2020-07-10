from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns index page and it's data
    '''
    title = "Home - Welcome to the best Movie Review Website Online"
    message = "Hello World!!!!"
    return render_template('index.html', title = title, message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns movie details page and its data
    '''
    return render_template('movie.html', id = movie_id)