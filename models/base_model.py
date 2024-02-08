#!/usr/bin/python3
""" base model """


import uuid
from datetime import datetime
import time
from models import storage



class BaseModel:
    """basemodel class"""

    def __init__(self, *args, **kwargs):
        """init method"""

        if kwargs:
            self.id = kwargs.get('id')
            self.created_at = datetime.fromisoformat(kwargs.get('created_at'))
            self.updated_at = datetime.fromisoformat(kwargs.get('updated_at'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string rep of class"""

        x = self.__class__.__name__
        return f"[{x}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""

        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        d['created_at'] =  self.created_at.isoformat()
        d['updated_at'] =  self.updated_at.isoformat()
        return d
