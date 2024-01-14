#!/usr/bin/python3
"""
The module for the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
