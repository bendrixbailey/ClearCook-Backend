# from azure.cosmos import CosmosClient, PartitionKey
# from azure.cosmos.exceptions import *
# import urllib.parse
# import json
# import random


# def create_database(client, db_name):
#     try:
#         client.create_database(id=db_name)
#     except CosmosResourceExistsError:
#         print("A database with this id already exists")


# def create_container(client, container_name):
#     try:
#         container = client.create_container(
#             id=container_name, partition_key=PartitionKey(path="/recipes")
#         )
#     except CosmosResourceExistsError:
#         container = client.get_container_client(container_name)

# def execute_query_no_var(container, query):
#     items = list(container.query_items(
#         query=query,
#         enable_cross_partition_query=True
#     ))

#     return items

# def get_recipe_by_id_short(container, id):
#     return list(container.query_items(
#         query='SELECT c.id, c.name, c.prepTime, c.imageLink FROM c WHERE c.id = "_r{}"'.format(id),
#         enable_cross_partition_query=True
#     ))

# def get_recipe_by_id_long(container, id):
#     return list(container.query_items(
#         query='SELECT * FROM c WHERE c.id = "_r{}"'.format(id),
#         enable_cross_partition_query=True
#     ))

# def get_recipe_by_exact_name(container, name):
#     print((urllib.parse.unquote_plus(name)))
#     return list(container.query_items(
#         query='SELECT * FROM c WHERE c.name = "{}"'.format(urllib.parse.unquote_plus(name)),
#         enable_cross_partition_query=True
#     ))

# def search_recipe_rough_name(container, rough_name):
#     print((urllib.parse.unquote_plus(rough_name)))
#     return list(container.query_items(
#         query='SELECT * FROM c WHERE UPPER(c.name) LIKE UPPER("%{}%")'.format(urllib.parse.unquote_plus(rough_name)),
#         enable_cross_partition_query=True
#     ))

# def get_random_recipes(container):
#     recipes = []
#     recipeCount = execute_query_no_var(container, "SELECT VALUE COUNT(1) FROM c")[0] - 1
#     print(recipeCount)
#     for recipe in range(4):
#         tempr = get_recipe_by_id_short(container, random.randint(0, recipeCount))[0]
#         print(tempr)
#         recipes.append(tempr)
#     return recipes
