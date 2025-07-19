# tests/test_select_courses.py

import unittest
from unittest.mock import patch
from app.select_courses import get_course_count_from_user

class TestSelectCourses(unittest.TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_valid_input(self, mock_input):
        self.assertEqual(get_course_count_from_user(5), 3)

    @patch('builtins.input', side_effect=['0', '6', '2'])
    def test_invalid_then_valid_input(self, mock_input):
        self.assertEqual(get_course_count_from_user(5), 2)

    @patch('builtins.input', side_effect=['abc', '3'])
    def test_non_integer_then_valid(self, mock_input):
        self.assertEqual(get_course_count_from_user(5), 3)

if __name__ == '__main__':
    unittest.main()
