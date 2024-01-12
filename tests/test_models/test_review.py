#!/usr/bin/python3
"""
Unittest for the Review module (Review Class)
"""
import unittest
import os
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """
    Test case class for the Review model.

    Methods:
        setUp(self): Set up a clean environment before each test.
        tearDown(self): Clean up the environment after each test.
        test_instance_creation(self): Test creating an instance of Review.
        test_attributes(self): Test Review instance attributes.
        test_str_representation(self): Test the __str__ method of Review.
        test_save_and_reload(self): Test saving and reloading Review
                                    instances from file.
        test_invalid_attribute(self): Test setting an invalid attribute
                                      for Review.
    """
    def setUp(self):
        """
        Set up a clean environment before each test.
        """
        storage.reload()  # Ensure a clean storage state
        self.test_review = Review()

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
        Test creating an instance of Review.
        """
        self.assertIsInstance(self.test_review, Review)

    def test_attributes(self):
        """
        Test Review instance attributes.
        """
        self.assertEqual(self.test_review.place_id, "")
        self.assertEqual(self.test_review.user_id, "")
        self.assertEqual(self.test_review.text, "")

    def test_str_representation(self):
        """
        Test the __str__ method of Review.
        """
        expected_str = (
                f"[Review] ({self.test_review.id}) "
                f"{self.test_review.__dict__}"
                )
        self.assertEqual(str(self.test_review), expected_str)

    def test_save_and_reload(self):
        """
        Test saving and reloading Review instances from file.
        """
        review_id = self.test_review.id
        self.test_review.place_id = "123"
        self.test_review.user_id = "456"
        self.test_review.text = "Great experience!"

        self.test_review.save()

        # Create a new Review instance and reload data from file
        new_review = Review()
        new_review.save()
        storage.reload()
        key = "Review.{}".format(review_id)
        reloaded_review = storage.all().get(key)

        self.assertIsNotNone(reloaded_review)
        self.assertEqual(self.test_review.id, reloaded_review.id)
        self.assertEqual(self.test_review.place_id, reloaded_review.place_id)
        self.assertEqual(self.test_review.user_id, reloaded_review.user_id)
        self.assertEqual(self.test_review.text, reloaded_review.text)


if __name__ == "__main__":
    unittest.main()
