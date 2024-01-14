#!/usr/bin/python3
"""
The module for the Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review.

    Attributes:
        place_id (str): The id of the place reviewed.
        user_id (str): The id of the user that did the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
