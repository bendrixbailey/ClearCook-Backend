import os
from flask import Flask
from flask_restful import Resource, Api

from api.clearcookAPI import *


app = Flask(__name__)
api = Api(app)

api.add_resource(Homepage, '/home')
api.add_resource(Recipes, '/recipes/<recipe_id>')

if __name__ == '__main__':
    
    app.run(debug=True)