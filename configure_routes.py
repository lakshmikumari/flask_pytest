from flask import request
from flask import jsonify
import json

books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Havard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]

def routes(app):
    @app.route("/bookapi")
    def get_books():
        """ function to get all books """
        print(f"BOOKS :{books}")
        print(books)
        print(jsonify({"Books": books}))
        return jsonify({"Books": books})

    @app.route("/hello")
    def hello():
        return("Hi Lakshmikumari")
