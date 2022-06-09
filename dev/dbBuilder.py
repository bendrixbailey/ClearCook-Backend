from codecs import getreader
from email.policy import default
from azure.cosmos import CosmosClient
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import json
import configparser

#connect to cosmos db database
config = configparser.ConfigParser()
config.read('../config.ini')
client = CosmosClient(
    config['recipedb']['uri'],
    config['recipedb']['primarykey']
)

#recipe json fields
recipe = {
    "id" : "",
    "name" : "",
    "prepTime": 0,
    "imageLink": "",
    "categories" : [],
    "ingredients" : [
        {
            "item": "",
            "quantity": ""
        }
    ],
    "steps": []
}

#user json fields
user = {
    "id" : 0,   #This is a required field, if it doesnt exist, it wont allow any items to be uploaded
    "name": "",
    "username" : "",
    "favorites" : [],
    "search-history" : []
}

clearcookDB = client.get_database_client(config['recipedb']['dbname'])


#Function makes a new recipedb and fills it with the data in testdata.json
def make_recipe_container():
    try:
        rcontainer = clearcookDB.create_container(id=config['recipedb']['containername'], partition_key=PartitionKey(path="/name"))
        return rcontainer
    except exceptions.CosmosResourceExistsError:
        return

#Function makes a new userdb and fills it with data in testuserdata.json
def make_user_container():
    try:
        ucontainer = clearcookDB.create_container(id=config['userdb']['containername'], partition_key=PartitionKey(path="/name"))
        return ucontainer
    except exceptions.CosmosResourceExistsError:
        return

def fill_container_with_data(container, datafile):
    d_file = open(datafile)
    d_json = json.load(d_file)
    for j_obj in d_json:
        try:
            container.upsert_item(j_obj)
        except exceptions.CosmosHttpResponseError:
            print("There was an error uploading <{}> to the database. Please ensure the object has valid".format(j_obj))
        # print(j_obj)

def delete_recipe_container():
    try:
        clearcookDB.delete_container(config['recipedb']['containername'])
    except exceptions.CosmosResourceNotFoundError:
        print("Recipe container does not exist, so cannot be deleted.")

def delete_user_container():
    try:
        clearcookDB.delete_container(config['userdb']['containername'])
    except exceptions.CosmosResourceNotFoundError:
        print("User container does not exist, so cannot be deleted.")

def get_recipe_container():
    try:
        return clearcookDB.get_container_client(config['recipedb']['containername'])
    except exceptions.CosmosResourceNotFoundError:
        print("Recipe container does not exist, so cannot be deleted.")

def get_user_container():
    try:
        return clearcookDB.get_container_client(config['userdb']['containername'])
    except exceptions.CosmosResourceNotFoundError:
        print("User container does not exist, so cannot be deleted.")

def update_db_schema(db, new_schema):
    for line in new_schema:
        return
    

def main():
    command = ""
    print("\
        Welcome to the development db manager for the ClearCook Backend\n\
        This tool has the following commands:\n\
        -    delete: clears both databases, including ALL data\n\
        -    delete -r: clears the recipe database\n\
        -    delete -u: clears user database\n\
        -    rebuild: rebuilds both user and populates with test data.\n\
        -    rebuild -r: rebuilds and fills recipe database\n\
        -    rebuild -u: rebuilds and fills user database\n\
        -    updateschema: updates the schema of the data in both databases\n\
        -    exit: exits this program\n\
        ")
    while(command != "exit"):
        command = input(">")
        match command:
            case "delete":
                delete_recipe_container()
                delete_user_container()
                print("Databases deleted successfully!")
                
            case "delete -r":
                delete_recipe_container()
                print("Deleted recipe database successfully!")
                
            case "delete -u":
                delete_user_container()
                print("Deleted user database successfully!")
                
            case "rebuild":
                delete_recipe_container()
                delete_user_container()
                t_r_container = make_recipe_container()
                fill_container_with_data(t_r_container, "testdata.json")
                print("{} has been rebuilt.".format(config['recipedb']['containername']))
                t_u_container = make_user_container()
                fill_container_with_data(t_u_container, "userdata.json")
                print("{} has been rebuilt.".format(config['userdb']['containername']))
                
            case "rebuild -r":
                delete_recipe_container()
                t_r_container = make_recipe_container()
                fill_container_with_data(t_r_container, "testdata.json")
                print("{} has been filled.".format(config['recipedb']['containername']))
                
            case "rebuild -u":
                delete_user_container()
                t_u_container = make_user_container()
                if(t_u_container == None):
                    t_u_container = get_user_container()
                fill_container_with_data(t_u_container, "userdata.json")
                print("{} has been filled.".format(config['userdb']['containername']))

            case "exit":
                return

            case _:
                print("Command not recognized, please enter a valid command")
    return


main()