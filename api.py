from flasterisk import Flasterisk
from flask import request, jsonify

class Api(Flasterisk):
    def __init__(self):
        Flasterisk.__init__(self,"api")

    def hello(self):
        return jsonify(status=200,message="Hello!")
