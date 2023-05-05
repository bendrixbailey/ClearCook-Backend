from pymongo import MongoClient
import json
import configparser

#connect to cosmos db database
env = "local"

config = configparser.ConfigParser()
config.read('../config.ini')
client = MongoClient(config[env]["host"])

#recipe json fields
recipe = {
    "num" : "",
    "name" : "",
    "prepTime": 0,
    "imageLink": "",
    "categories" : [],
    "ingredients" : [],
    "steps": [],
    "rating" : {
        "stars" : 0,
        "ratings" : 0
    }
}

clearcookDB = client[config[env]["dbname"]]
recipedb = clearcookDB[config[env]["recipe"]]

def make_recipe_collection():
    recipedb = clearcookDB[config[env]["recipes"]]


def fill_collection_with_data(collection, datafile):
    d_file = open(datafile)
    d_json = json.load(d_file)
    for j_obj in d_json:
        collection.insert_one(j_obj)

def delete_recipe_container():
    clearcookDB.drop_collection(config[env]["recipes"])    

def main():
    command = ""
    print("\
        Welcome to the development db manager for the ClearCook Backend\n\
        This tool has the following commands:\n\
        -    delete: clears both databases, including ALL data\n\
        -    rebuild: rebuilds both user and populates with test data.\n\
        -    exit: exits this program\n\
        ")
    while(command != "exit"):
        command = input(">")
        match command:
            case "delete":
                delete_recipe_container()
                print("Databases deleted successfully!")

            case "rebuild":
                delete_recipe_container()
                t_r_container = make_recipe_collection()
                fill_collection_with_data(t_r_container, "testdata.json")
                print("{} has been rebuilt.".format(config['recipedb']['containername']))
                # t_u_container = make_user_container()
                # fill_container_with_data(t_u_container, "userdata.json")
                # print("{} has been rebuilt.".format(config['userdb']['containername']))
                
            # case "rebuild -u":
            #     delete_user_container()
            #     t_u_container = make_user_container()
            #     if(t_u_container == None):
            #         t_u_container = get_user_container()
            #     fill_container_with_data(t_u_container, "userdata.json")
            #     print("{} has been filled.".format(config['userdb']['containername']))

            case "exit":
                return

            case _:
                print("Command not recognized, please enter a valid command")
    return


main()