from typing import Any
import pymongo
import json
import random
from bson import json_util
from bson import ObjectId


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        # return json.JSONEncoder.default(self, o)
        return str(o)



def execute_query_no_variable():
    return

def get_all_recipes(collection):
    try:
        results = list(collection.find())
        return json.loads(MongoJSONEncoder().encode(results))
    except Exception as e:
        return e

def get_recipe_by_id_short(collection, id):
    #.find does not encode properly, so we have to manually do it.
    return json.loads(MongoJSONEncoder().encode(list(collection.find({"index" : id}, {"index" : 1, "name" : 1, "prepTime" : 1, "imageLink" : 1}))))

def get_recipe_by_id_long(collection, id=int):
    #find_one already encodes, we just have to omit the _id field, as its not serializable
    recipes = collection.find_one({"index" : int(id)}, {"_id" : 0})
    if(recipes != None):
        return recipes
    else:
        return "No recipes found for that id"

def search_recipe_by_exact_name(collection, name):
    return json.loads(MongoJSONEncoder().encode(list(collection.find({"name" : name}))))

def search_recipe_rough_name(collection, roughname):
    try:
        results = list(collection.find({"name" : {"$regex" : ("^(?i).*" + roughname + ".*$")}}))

        if(len(results) > 0):
            return json.loads(MongoJSONEncoder().encode(results))
        else:
            return "No recipe found containing that query."
        
    except Exception as e:
        return e
    

def add_recipe_by_link():
    # add in call to run the recipescanner
    return

def update_recipe():
    return

def get_random_recipes(collection, count=4):
    recipes = []
    recipecont = collection.count_documents({})
    indexes = random.sample(range(0, recipecont-1), count)
    for index in indexes:
        #print(get_recipe_by_id_long(collection, index))
        recipes.append(get_recipe_by_id_short(collection, index)[0])
        
    return recipes

    