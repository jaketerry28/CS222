import unittest
from unittest.mock import patch
from app.register_courses import register_for_courses
from app.Course import Course

class TestRegisterCourses(unittest.TestCase):
    def setUp(self):
        self.offered_courses = {
            "CS101": [
                Course("CS101", "001", "MWF", "0900", "0950"),
                Course("CS101", "101", "MWF", "1300", "1350")
            ],
            "MATH201": [
                Course("MATH201", "002", "TR", "1000", "1115")
            ]
        }

    # test that courses can be registered successfully
    @patch("builtins.input", side_effect=["CS101", "MATH201"])
    @patch("builtins.print")
    def test_prompt_n_courses(self, mock_print, mock_input):
        registered_courses = []
        register_for_courses(self.offered_courses, 2, registered_courses)

        self.assertEqual(len(registered_courses), 2)
        self.assertEqual(registered_courses[0], "CS101")
        self.assertEqual(registered_courses[1], "MATH201")
    
    # test that duplicate course registrations are handled correctly
    @patch("builtins.input", side_effect=["CS101","CS101", "MATH201",])
    @patch("builtins.print")
    def test_already_registered(self, mock_print, mock_input):
        registered_courses = []
        register_for_courses(self.offered_courses, 2, registered_courses)

        # Only 2 courses should be registered total: first CS101, then MATH201 (after duplicate rejected)
        self.assertEqual(len(registered_courses), 2)
        self.assertEqual(registered_courses[0], "CS101")
        self.assertEqual(registered_courses[1], "MATH201")

        # Check that the duplicate message was printed
        mock_print.assert_any_call("\nAlready registered for that course. Please choose a different one.")

    # test that invalid course IDs are handled correctly
    @patch("builtins.input", side_effect=["CS999", "CS101", "001"])
    @patch("builtins.print")
    def test_invalid_course_id(self, mock_print, mock_input):
        registered_courses = []
        register_for_courses(self.offered_courses, 1, registered_courses)

if __name__ == '__main__':
    unittest.main()
