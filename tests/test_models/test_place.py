#!/usr/bin/python3
"""
Unittest for the Place module (Place Class)
"""
import unittest
import os
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """
    Test case class for the Place model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of Place.
        test_attributes(self): Test Place instance attributes.
        test_str_representation(self): Test the __str__ method of Place.
        test_save_and_reload(self): Test saving and reloading Place instances from file.
        test_invalid_attribute(self): Test setting an invalid attribute for Place.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensure a clean storage state
        self.test_place = Place()

    def tearDown(self):
        """
        Clean up the environment after each test.
        """
        try:
            os.remove("file.json")  # Remove the test file after each test
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """
        Test creating an instance of Place.
        """
        self.assertIsInstance(self.test_place, Place)

    def test_attributes(self):
        """
        Test Place instance attributes.
        """
        self.assertEqual(self.test_place.city_id, "")
        self.assertEqual(self.test_place.user_id, "")
        self.assertEqual(self.test_place.name, "")
        self.assertEqual(self.test_place.description, "")
        self.assertEqual(self.test_place.number_rooms, 0)
        self.assertEqual(self.test_place.number_bathrooms, 0)
        self.assertEqual(self.test_place.max_guest, 0)
        self.assertEqual(self.test_place.price_by_night, 0)
        self.assertEqual(self.test_place.latitude, 0.0)
        self.assertEqual(self.test_place.longitude, 0.0)
        self.assertEqual(self.test_place.amenity_ids, [])

    def test_str_representation(self):
        """
        Test the __str__ method of Place.
        """
        expected_str = f"[Place] ({self.test_place.id}) {self.test_place.__dict__}"
        self.assertEqual(str(self.test_place), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading Place instances from file.
        """
        place_id = self.test_place.id
        self.test_place.city_id = "123"
        self.test_place.user_id = "456"
        self.test_place.name = "Cozy Cabin"
        self.test_place.description = "A rustic retreat"
        self.test_place.number_rooms = 2
        self.test_place.number_bathrooms = 1
        self.test_place.max_guest = 4
        self.test_place.price_by_night = 100
        self.test_place.latitude = 37.7749
        self.test_place.longitude = -122.4194
        self.test_place.amenity_ids = ["789", "101"]

        self.test_place.save()

        # Create a new Place instance and reload data from file
        new_place = Place()
        new_place.save()
        storage.reload()
        key = "Place.{}".format(place_id)
        reloaded_place = storage.all().get(key)

        self.assertIsNotNone(reloaded_place)
        self.assertEqual(self.test_place.id, reloaded_place.id)
        self.assertEqual(self.test_place.city_id, reloaded_place.city_id)
        self.assertEqual(self.test_place.user_id, reloaded_place.user_id)
        self.assertEqual(self.test_place.name, reloaded_place.name)
        self.assertEqual(self.test_place.description, reloaded_place.description)
        self.assertEqual(self.test_place.number_rooms, reloaded_place.number_rooms)
        self.assertEqual(self.test_place.number_bathrooms, reloaded_place.number_bathrooms)
        self.assertEqual(self.test_place.max_guest, reloaded_place.max_guest)
        self.assertEqual(self.test_place.price_by_night, reloaded_place.price_by_night)
        self.assertEqual(self.test_place.latitude, reloaded_place.latitude)
        self.assertEqual(self.test_place.longitude, reloaded_place.longitude)
        self.assertEqual(self.test_place.amenity_ids, reloaded_place.amenity_ids)


if __name__ == "__main__":
    unittest.main()
