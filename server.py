import os
from flask import Flask
from flask_restful import Resource, Api
import configparser

from api.clearcookAPI import *


app = Flask(__name__)
api = Api(app)

api.add_resource(Homepage, '/home')
api.add_resource(AllRecipes, '/recipes', endpoint = 'recipes')
api.add_resource(RecipeById, '/recipes/<id>')
api.add_resource(RecipeByName, '/recipes/name/<name>')




if __name__ == '__main__':
    
    app.run(debug=True)