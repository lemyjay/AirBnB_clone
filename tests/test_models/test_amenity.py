#!/usr/bin/python3
"""
Unittest for the Amenity module (Amenity Class)
"""
import unittest
import os
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
    Test case class for the Amenity model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of Amenity.
        test_attributes(self): Test Amenity instance attributes.
        test_str_representation(self): Test the __str__ method of Amenity.
        test_save_and_reload(self): Test saving and reloading Amenity instances from file.
        test_invalid_attribute(self): Test setting an invalid attribute for Amenity.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensures a clean storage state
        self.test_amenity = Amenity()

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
        Test creating an instance of Amenity.
        """
        self.assertIsInstance(self.test_amenity, Amenity)

    def test_attributes(self):
        """
        Test Amenity instance attributes.
        """
        self.assertEqual(self.test_amenity.name, "")

    def test_str_representation(self):
        """
        Test the __str__ method of Amenity.
        """
        expected_str = f"[Amenity] ({self.test_amenity.id}) {self.test_amenity.__dict__}"
        self.assertEqual(str(self.test_amenity), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading Amenity instances from file.
        """
        amenity_id = self.test_amenity.id
        self.test_amenity.name = "Swimming Pool"
        self.test_amenity.save()

        # Create a new Amenity instance and reload data from file
        new_amenity = Amenity()
        new_amenity.save()
        storage.reload()
        key = "Amenity.{}".format(amenity_id)
        reloaded_amenity = storage.all().get(key)

        self.assertIsNotNone(reloaded_amenity)
        self.assertEqual(self.test_amenity.id, reloaded_amenity.id)
        self.assertEqual(self.test_amenity.name, reloaded_amenity.name)

    def test_invalid_attribute(self):
        """
        Test setting an invalid attribute for Amenity.
        """
        with self.assertRaises(AttributeError):
            self.test_amenity.invalid_attribute = "value"


if __name__ == "__main__":
    unittest.main()
