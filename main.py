from flask import Flask
from flask_restful import Resource, Api
from services.read_file import read_file
from classes.movie import Movie


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        data = read_file('./data/movies.csv')
        movies = list()
        for row in data:
            movies.append(Movie(row.split(',')[0], row.split(',')[1], row.split(',')[2]).__dict__)
        return movies


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
