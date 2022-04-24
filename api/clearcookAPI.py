from distutils.command.config import config
from flask_restful import Resource, request, reqparse
from azure.cosmos import CosmosClient, PartitionKey
import os
import json
import config

from src.db_util_functions import *

parser = reqparse.RequestParser()

client = CosmosClient(
    config.settings['uri'], 
    config.settings['primary_key']
)

#
class Homepage(Resource):
    def get(self):
        return {'hello'}

#This is how to get data for each recipe stored in the database
class Recipes(Resource):
    def get(self, recipe_id):
        return {}
