from distutils.command.config import config
from flask_restful import Resource, request, reqparse
from azure.cosmos import CosmosClient, PartitionKey
import os
import json
import config

from src.cosmos_db_functions import *

parser = reqparse.RequestParser()

client = CosmosClient(
    config.settings['uri'], 
    config.settings['primary_key']
)

recipeDB = client.get_database_client(config.settings['recipeDBName'])
recipeContainer = recipeDB.get_container_client(config.settings['recipeContainerName'])


#
class Homepage(Resource):
    def get(self):
        response = get_random_recipes(recipeContainer)
        return response
        # return response
        # return recipeContainer.id

#This is how to get data for each recipe stored in the database
class Recipes(Resource):
    def get(self, recipe_id):
        return ''

    def get(self):
        response = execute_query_no_var(recipeContainer, "SELECT * FROM c")
        return response
    
