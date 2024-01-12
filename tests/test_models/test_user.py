#!/usr/bin/python3
"""
Unittest for the User module (User Class)
"""
import unittest
import os
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """
    Test case class for the User model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of User.
        test_attributes(self): Test User instance attributes.
        test_str_representation(self): Test the __str__ method of User.
        test_save_and_reload(self): Test saving and reloading User
                                    instances from file.
        test_invalid_attribute(self): Test setting an invalid attribute
                                      for User.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensures a clean storage state
        self.test_user = User()

    def tearDown(self):
        """
        Clean up the environment after each test.
        """
        try:
            os.remove("file.json")  # Removes the test file after each test
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """
        Test creating an instance of User.
        """
        self.assertIsInstance(self.test_user, User)

    def test_attributes(self):
        """
        Test User instance attributes.
        """
        self.assertEqual(self.test_user.email, "")
        self.assertEqual(self.test_user.password, "")
        self.assertEqual(self.test_user.first_name, "")
        self.assertEqual(self.test_user.last_name, "")

    def test_str_representation(self):
        """
        Test the __str__ method of User.
        """
        expected_str = (
                f"[User] ({self.test_user.id}) "
                f"{self.test_user.__dict__}"
                )
        self.assertEqual(str(self.test_user), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading User instances from file.
        """
        user_id = self.test_user.id
        self.test_user.email = "test@example.com"
        self.test_user.password = "password123"
        self.test_user.first_name = "John"
        self.test_user.last_name = "Doe"
        self.test_user.save()

        new_user = User()
        new_user.save()
        storage.reload()
        key = "User.{}".format(user_id)
        reloaded_user = storage.all().get(key)

        self.assertIsNotNone(reloaded_user)
        self.assertEqual(self.test_user.id, reloaded_user.id)
        self.assertEqual(self.test_user.email, reloaded_user.email)
        self.assertEqual(self.test_user.password, reloaded_user.password)
        self.assertEqual(self.test_user.first_name, reloaded_user.first_name)
        self.assertEqual(self.test_user.last_name, reloaded_user.last_name)


if __name__ == "__main__":
    unittest.main()
