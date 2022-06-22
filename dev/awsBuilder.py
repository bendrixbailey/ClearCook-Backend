import configparser
import json
import pymongo
import sys

config = configparser.ConfigParser()
config.read('../azureconfig.ini')

client = pymongo.MongoClient(config["recipedb"]["uri"])
print(client.list_database_names())
client.close()
# recipedb = client.clearcook
