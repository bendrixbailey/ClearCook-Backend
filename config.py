#port: 3306

from curses import KEY_SF
from inspect import EndOfBlock
import os
from re import S
from tkinter import W

from pkg_resources import ensure_directory

settings = {
    'host' : 'clearcookdb.mongo.cosmos.azure.com',
    'username' : 'clearcookdb',
    'primary_key' : 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==',
    'uri': 'https://localhost:8081',
}