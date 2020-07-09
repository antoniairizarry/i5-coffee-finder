from flask import Blueprint, jsonify, request
from . import db 
from .models import Movie

main = Blueprint('main', __name__)

#**********NOTE!!!!**********
#Can/may need to seperate routes but this is 2 routes from youtube
#to add movie (post)
#list movies (get)
#****************************

#POST: /add_movie
#to add movie to db
@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


#GET: /movies
#list all movies
@main.route('/movies')
def movies():
    movies = ['hi']
    #TODO: UNCOMMENT THIS ONCE DB IS HOOKED UP
    # movie_list = Movie.query.all()
    # for movie in movie_list:
    #     movies.append({'title' : movie.title, 'rating' : movie.rating})
    return jsonify({'movies' : movies})

#GET: /
#index page
@main.route('/', methods=['GET'])
def home():
    return "<h1>!Starbucks Coffee Shop App</h1><p>bunch of stuff here later</p>"