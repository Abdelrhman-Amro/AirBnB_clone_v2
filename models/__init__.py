#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage as fs
from models.engine.db_storage import DBStorage as db
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = db()
else:
    storage = fs()
storage.reload()
