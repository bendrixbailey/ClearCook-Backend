from azure.cosmos import CosmosClient, PartitionKey
from azure.cosmos.exceptions import *



def create_database(client, db_name):
    try:
        client.create_database(id=db_name)
    except CosmosResourceExistsError:
        print("A database with this id already exists")


def create_container(client, container_name):
    try:
        container = client.create_container(
            id=container_name, partition_key=PartitionKey(path="/recipes")
        )
    except CosmosResourceExistsError:
        container = client.get_container_client(container_name)

def get_random_recipes(client, container_name):
    return ""

def execute_query(container, query):
    container.query_items(
        query=query,
        enable_cross_partition_query=True
    )
