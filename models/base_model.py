#!/usr/bin/python3


import uuid
from datetime import datetime
import time
import models


class BaseModel:
    """basemodel class"""

    def __init__(self, **kwargs):
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

        d = {}
        d['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()
            else:
                d[k] = v
        return d
