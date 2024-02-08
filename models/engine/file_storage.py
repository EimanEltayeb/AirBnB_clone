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
        de_clss = {'BaseModel': models.base_model.BaseModel}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                ob_dic = json.load(f)
                for o_v in ob_dic.values():
                    cls_name = o_v["__class__"]
                    cls_obj = de_clss[cls_name]
                    self.new(cls_obj(**o_v))
                FileStorage.__objects 
        except FileNotFoundError:
            pass
