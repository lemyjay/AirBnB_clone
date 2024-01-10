#!/usr/bin/python3
"""
Unittest for the BaseModel module (Base Class)
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage



class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.

    This test suite covers various aspects of the BaseModel class,
    including instance creation, ID uniqueness, attribute types,
    methods like to_dict and __str__, and updating attributes.

    To run these tests, use `python3 -m unittest test_base_model.py`.
    """

    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_id_uniqueness(self):
        """Test the uniqueness of the generated IDs."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_updated_at_types(self):
        """Test the types of 'created_at' and 'updated_at' attributes."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)

    def test_str_representation(self):
        """Test the __str__ method."""
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIsInstance(str_representation, str)
        self.assertIn('[BaseModel]', str_representation)
        self.assertIn(my_model.id, str_representation)

    def test_update_attributes(self):
        """Test updating attributes of the BaseModel instance."""
        my_model = BaseModel()
        my_model.name = "Test"
        my_model.number = 42

        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(hasattr(my_model, 'number'))
        self.assertEqual(my_model.name, "Test")
        self.assertEqual(my_model.number, 42)

    def test_save_reload(self):
        """Test saving and reloading from file."""
        my_model = BaseModel()
        my_model.save()
        storage.reload()
        reloaded_model = storage.all().get(f"BaseModel.{my_model.id}")

        self.assertIsNotNone(reloaded_model)
        self.assertEqual(my_model.id, reloaded_model.id)
        self.assertEqual(my_model.created_at, reloaded_model.created_at)
        self.assertEqual(my_model.updated_at, reloaded_model.updated_at)

    def test_save_reload_with_changes(self):
        """Test saving, reloading, and updating attributes."""
        my_model = BaseModel()
        my_model.save()
        storage.reload()
        reloaded_model = storage.all().get(f"BaseModel.{my_model.id}")

        self.assertIsNotNone(reloaded_model)
        self.assertEqual(my_model.id, reloaded_model.id)
        self.assertEqual(my_model.created_at, reloaded_model.created_at)
        self.assertEqual(my_model.updated_at, reloaded_model.updated_at)

        # Make changes and save again
        reloaded_model.name = "Updated Name"
        reloaded_model.save()
        storage.reload()
        updated_model = storage.all().get(f"BaseModel.{reloaded_model.id}")

        self.assertIsNotNone(updated_model)
        self.assertEqual(reloaded_model.id, updated_model.id)
        self.assertEqual(reloaded_model.updated_at, updated_model.updated_at)
        self.assertEqual(reloaded_model.name, updated_model.name)

    def test_reload_nonexistent_file(self):
        """Test reloading from a non-existent file."""
        non_existent_file_path = "non_existent_file.json"
        storage.__file_path = non_existent_file_path

        with self.assertRaises(FileNotFoundError):
            storage.reload()

if __name__ == '__main__':
    unittest.main()