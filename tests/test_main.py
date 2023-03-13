from flask import Flask
import json
import pytest

from flask_pytest.configure_routes import routes

#from api import app

def test_hello():
    app=Flask(__name__)
    routes(app)
    client=app.test_client()
    url="/hello"
    response = client.get(url)
    assert response.get_data() == b'Hi Lakshmikumari'
    assert response.status_code == 200


def test_books():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()
    url="/bookapi"
    response = client.get(url)
    res = json.loads(response.data.decode('utf-8')).get("Books")


    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    #assert res.status_code == 200
    assert type(res) is list

