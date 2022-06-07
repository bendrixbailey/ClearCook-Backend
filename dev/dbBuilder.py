from azure.cosmos import CosmosClient
import configparser

#connect to cosmos db database
config = configparser.ConfigParser()
config.read('config.ini')
client = CosmosClient(
    config['recipedb']['uri'],
    config['recipedb']['primarykey']
)


def main():
    #set up commands for rebuilding db, reloading items, and deleting everythigg
    return


main()