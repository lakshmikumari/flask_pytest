# get books data
from flask import Flask
from configure_routes import routes
from flask import jsonify
app = Flask(__name__)

routes(app)

if __name__ == '__main__':
    app.run()

