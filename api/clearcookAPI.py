from flask_restful import Resource, request, reqparse
import os
import json
import configparser
from pymongo import MongoClient

from src.mongodbFunctions import *

parser = reqparse.RequestParser()
config = configparser.ConfigParser()
config.read('config.ini')
env = "local"

client = MongoClient([config[env]["host"]])



recipeDB = client[config[env]["dbname"]]
recipeContainer = recipeDB[config[env]["recipes"]]


#
class Homepage(Resource):
    def get(self):
        response = get_random_recipes(recipeContainer)
        return response

#This is how to get data for each recipe stored in the database
class AllRecipes(Resource):
    def get(self):
        response = get_all_recipes(recipeContainer)
        return response

class RecipeById(Resource):
    def get(self, id):
        return get_recipe_by_id_long(recipeContainer, id)

class RecipesByName(Resource):
    def get(self, name):
        return search_recipe_rough_name(recipeContainer, name)

class RecipeByFullName(Resource):
    def get(self, name):
        return search_recipe_rough_name(recipeContainer, name)[0]
