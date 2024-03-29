#!/usr/bin/python3
""" engine"""


import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj with key"""

        c = obj.__class__.__name__
        FileStorage.__objects[f"{c}.{obj.id}"] = obj

    def save(self):
        """ serialize objects to json file"""

        ob_dict = {}
        for key, v in FileStorage.__objects.items():
            ob_dict[key] = v.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(ob_dict, f)

    def reload(self):
        """deserializes the JSON file"""

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass
