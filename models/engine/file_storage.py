#!/usr/bin/python3
""" engine"""


import json


class FileStorage:
    """ FileStorage class """

    def __init__(self):
        """ init method"""

        self.__file_path = "file.json" 
        self.__objects = dict()

    @property
    def file_path(self):
        """ file_path getter"""

        return self.__file_path

    def all(self):
        """ returns the dictionary"""

        return self.__objects

    def new(self, obj):
        """sets obj with key"""

        c = self.__class__.__name__
        self.__objects[f"{c}.{self.id}"] = obj

    def save(self):
        """ serialize objects to json file"""

        with open(self.__file_path, "a") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file"""

        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f.read())
        except FileNotFoundError:
            pass
