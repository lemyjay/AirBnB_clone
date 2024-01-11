#!/usr/bin/python3
"""
The module for handling User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents a user in the system.

    Attributes:
        email (str): Email address of the user.
        password (str): Password associated with the user's account.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """
        Returns the string representation of the User instance.

        Returns:
            str: String representation of the User.
        """
        return "[User] ({}) {}".format(self.id, self.__dict__)
