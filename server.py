import os
from flask import Flask
from flask_restful import Resource, Api
import configparser

from api.clearcookAPI import *


app = Flask(__name__)
api = Api(app)
config = configparser.ConfigParser()
config.read('config.ini')

api.add_resource(Homepage, '/home')
api.add_resource(Recipes, '/recipes/<recipe_id>')


client = CosmosClient(
    config['recipedb']['uri'],
    config['recipedb']['primarykey']
)

if __name__ == '__main__':
    
    app.run(debug=True)