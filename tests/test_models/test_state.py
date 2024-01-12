#!/usr/bin/python3
"""
Unittest for the State module (State Class)
"""
import unittest
import os
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    Test case class for the State model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of State.
        test_attributes(self): Test State instance attributes.
        test_str_representation(self): Test the __str__ method of State.
        test_save_and_reload(self): Test saving and reloading State instances from file.
        test_invalid_attribute(self): Test setting an invalid attribute for State.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensures a clean storage state
        self.test_state = State()

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
        Test creating an instance of State.
        """
        self.assertIsInstance(self.test_state, State)

    def test_attributes(self):
        """
        Test State instance attributes.
        """
        self.assertEqual(self.test_state.name, "")

    def test_str_representation(self):
        """
        Test the __str__ method of State.
        """
        expected_str = f"[State] ({self.test_state.id}) {self.test_state.__dict__}"
        self.assertEqual(str(self.test_state), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading State instances from file.
        """
        state_id = self.test_state.id
        self.test_state.name = "California"
        self.test_state.save()

        # Create a new State instance and reload data from file
        new_state = State()
        new_state.save()
        storage.reload()
        key = "State.{}".format(state_id)
        reloaded_state = storage.all().get(key)

        self.assertIsNotNone(reloaded_state)
        self.assertEqual(self.test_state.id, reloaded_state.id)
        self.assertEqual(self.test_state.name, reloaded_state.name)


if __name__ == "__main__":
    unittest.main()
