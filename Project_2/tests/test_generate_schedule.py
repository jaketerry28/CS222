import unittest
from app.Course import Course
from app.generate_schedule import *
class TestCourseOverlap(unittest.TestCase):
    
    def setUp(self):

        # overlaps exist between:
            # CS101 001, CS120 011
            # CS101 001, CS120 223
            # MATH201 002, CS120 563

        # valid schedule will be:
            #("CS101", "001", "MWF", "0900", "0950")
            #("MATH201", "003", "TR", "0800", "0850")
            #("CS120", "563", "TR", "1100", "1150")


        self.viable_schedule_can_be_made = {
            "CS101": [
                Course("CS101", "001", "MWF", "0900", "0950"),
                Course("CS101", "101", "MWF", "1300", "1350")
            ],
            "MATH201": [
                Course("MATH201", "002", "TR", "1000", "1115"),
                Course("MATH201", "003", "TR", "0800", "0850")
            ],
            "CS120": [  
                Course("CS120", "011", "MWF", "0900", "0950"),
                Course("CS120", "223", "MWF", "0930", "1020"),
                Course("CS120", "563", "TR", "1100", "1150")
            ]
        }

        # no schedule can be made from these 
        self.no_viable_schedule_can_be_made = {
            "CS101": [
                Course("CS101", "001", "MWF", "0900", "0950"),
                Course("CS101", "101", "MWF", "0930", "1020")
            ],
            "MATH201": [
                Course("MATH201", "002", "TR", "1000", "1115")
            ],
            "CS120": [  
                Course("CS120", "011", "MWF", "0900", "0950"),
                Course("CS120", "223", "MWF", "0930", "1020"),
                Course("CS120", "563", "TR", "1100", "1150")
            ]
        }

        # example user input
        self.selected_courses = ["CS101", "MATH201", "CS120"]

    def test_generate_success(self):
        #all_courses = list(self.offered_courses.items())
        schedule = generate_schedule({}, self.selected_courses, self.viable_schedule_can_be_made)

        self.assertEqual(len(schedule), 3)
        self.assertEqual(schedule['CS101'], Course("CS101", "001", 'MWF', "0900", "0950"))        
        self.assertEqual(schedule['MATH201'], Course("MATH201", "003", 'TR', "0800", "0850"))        
        self.assertEqual(schedule['CS120'], Course("CS120", "563", 'TR', "1100", "1150"))

    def test_generate_fail(self):
        schedule = generate_schedule({}, self.selected_courses, self.no_viable_schedule_can_be_made)
        self.assertIsNone(schedule)


if __name__ == '__main__':
    unittest.main()


