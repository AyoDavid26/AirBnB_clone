#!/usr/bin/python3
"""Defining the base model class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representing the BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializing a new BaseModel

        where:
            *args(any): Unused
            **kwargs (dict): key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Updating updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returning the dictionary of BaseModel instance

        Includes the key/value pair __class__ representing
        the class name of object"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the print/str rep of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
