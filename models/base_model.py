#!/usr/bin/python3
""" module that defines BaseModel class """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel that defines all common
    attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if (kwargs):
            """ re-create an instance with kwargs dictionary representation."""
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if ((key == "updated_at") or (key == "created_at")):
                    value = datetime.strptime(value, date_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def save(self):
        """ update public instance updated_at with current time """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ returns the dictornary representation of BaseModel
        instance with class name included """
        my_dict = dict()
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """ return the string representation of BaseModel instance """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
