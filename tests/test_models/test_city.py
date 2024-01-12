#!/usr/bin/python3
"""
Unittest for the City module (City Class)
"""
import unittest
import os
from models.city import City
from models import storage
from models.state import State


class TestCity(unittest.TestCase):
    """
    Test case class for the City model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of City.
        test_attributes(self): Test City instance attributes.
        test_str_representation(self): Test the __str__ method of City.
        test_save_and_reload(self): Test saving and reloading City instances
                                    from file.
        test_invalid_attribute(self): Test setting an invalid attribute
                                      for City.
        test_relationship_with_state(self): Test the relationship between
                                            City and State.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensures a clean storage state
        self.test_city = City()

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
        Test creating an instance of City.
        """
        self.assertIsInstance(self.test_city, City)

    def test_attributes(self):
        """
        Test City instance attributes.
        """
        self.assertEqual(self.test_city.state_id, "")
        self.assertEqual(self.test_city.name, "")

    def test_str_representation(self):
        """
        Test the __str__ method of City.
        """
        expected_str = (
                f"[City] ({self.test_city.id}) "
                f"{self.test_city.__dict__}"
                )
        self.assertEqual(str(self.test_city), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading City instances from file.
        """
        city_id = self.test_city.id
        self.test_city.state_id = "state_id_1"
        self.test_city.name = "San Francisco"
        self.test_city.save()

        # Create a new City instance and reload data from file
        new_city = City()
        new_city.save()
        storage.reload()
        key = "City.{}".format(city_id)
        reloaded_city = storage.all().get(key)

        self.assertIsNotNone(reloaded_city)
        self.assertEqual(self.test_city.id, reloaded_city.id)
        self.assertEqual(self.test_city.state_id, reloaded_city.state_id)
        self.assertEqual(self.test_city.name, reloaded_city.name)

    def test_relationship_with_state(self):
        """
        Test the relationship between City and State.
        """
        state = State()
        state.save()
        state_id = state.id

        city_id = self.test_city.id
        self.test_city.state_id = state_id
        self.test_city.save()

        # Reload data and check the relationship
        storage.reload()
        key = "City.{}".format(city_id)
        reloaded_city = storage.all().get(key)

        self.assertIsNotNone(reloaded_city)
        self.assertEqual(reloaded_city.state_id, state_id)


if __name__ == "__main__":
    unittest.main()
