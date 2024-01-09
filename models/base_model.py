#!/usr/bin/python3
"""
module that defines BaseModel class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        """
        Update public instance updated_at with current time
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        Returns the dictornary representation of BaseModel
        instance with class name included
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """
        Returns the string representation of BaseModel instance
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
