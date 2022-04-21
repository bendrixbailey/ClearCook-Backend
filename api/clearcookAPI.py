from flask_restful import Resource, request, reqparse
import os
import json

from src.db_util_functions import *

parser = reqparse.RequestParser()

#
class Homepage(Resource):
    def get(self):
        return {'hello'}

#This is how to get data for each recipe stored in the database
class Recipes(Resource):
    def get(self, recipe_id):
        return {}
