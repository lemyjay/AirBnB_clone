#!/usr/bin/python3
"""
module that defines BaseModel class
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel class defines all common attributes/methods
    for other classes


    Public instance attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The timestamp of when the instance was created.
        updated_at (datetime): The timestamp of the last update to the instance.

    Methods:
        __int__(self, *args, **kwargs): The class constructor.
        save(self): Updates public instance "updated_at" with current time
        to_dict(self): Returns the dictionary representation the Class with class name included
        __str__: Returns the string representation of BaseModel instance
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel

        Args:
        *args: Not used
        **kwargs: Dictionary representation of the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Update public instance updated_at with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the dictornary representation of BaseModel
        instance with class name included
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """
        Returns the string representation of BaseModel instance
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
