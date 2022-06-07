from distutils.command.config import config
from flask_restful import Resource, request, reqparse
from azure.cosmos import CosmosClient, PartitionKey
import os
import json
import configparser

from src.cosmos_db_functions import *

parser = reqparse.RequestParser()
config = configparser.ConfigParser()
config.read('config.ini')

client = CosmosClient(
    config['recipedb']['uri'],
    config['recipedb']['primarykey']
)

recipeDB = client.get_database_client(config.settings['recipeDBName'])
recipeContainer = recipeDB.get_container_client(config.settings['recipeContainerName'])


#
class Homepage(Resource):
    def get(self):
        response = get_random_recipes(recipeContainer)
        return response

#This is how to get data for each recipe stored in the database
class AllRecipes(Resource):
    def get(self):
        response = execute_query_no_var(recipeContainer, "SELECT * FROM c")
        return response

class RecipeById(Resource):
    def get(self, recipe_id):
        return get_recipe_by_id_long(recipeContainer, recipe_id)

class RecipeByName(Resource):
    def get(self, name):
        return search_recipe_rough_name(recipeContainer, name)
