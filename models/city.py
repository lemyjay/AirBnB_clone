#!/usr/bin/python3
"""
The module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city.

    Attributes:
        state_id (str): The state id to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
