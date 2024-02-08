#!/usr/bin/python3
""" engine"""


import json
import models


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

        ob_dict = {key: models.base_model.to_dict(v) for key, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(ob_dict, f)

    def reload(self):
        """deserializes the JSON file"""

        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
