import unittest
from unittest.mock import patch, mock_open
from app import view_courses
from app.Course import Course

# define a mock text file that has been read
TEST_TEXT_CONTENT = [
    "CS120\t10\tMWF\t0900\t0950\n",
    "CS120\t1\tMWF\t1000\t1050\n",
    "MATH166\t5\tTR\t1100\t1215\n"
]

# real file would be a continous string
MOCKED_DATA = "".join(TEST_TEXT_CONTENT)

class TestViewCourses(unittest.TestCase):

    def test_get_courses_existing_file(self):
        try:
            with patch('builtins.open', mock_open(read_data=MOCKED_DATA)) as m:
                courses = view_courses.get_courses("courses.txt")
        except:
            self.fail("This file did not open correctly")

        expected = TEST_TEXT_CONTENT
        self.assertEqual(courses, expected)

    def test_get_courses_bad_file(self):
        with self.assertRaises(FileNotFoundError):
            view_courses.get_courses("i_dont_exist.txt")
    
    def test_sort_key(self):
        # test multiple entries
        entries = [["MATH166", "007", "MWF", "1100", "1345"],
                            ["MATH166", "999", "MWF", "1100", "1345"],
                            ["CS222", "222", "MWF", "1100", "1345"],
                            ["ENG103", "028", "MWF", "1100", "1345"]]
        
        results = []
        # create Course objects
        for course in entries:
            # convert to Course object
            course_obj = view_courses.Course(*course)
            # get the sort key
            key = view_courses.sort_key(course_obj)
            results.append(key)
        
        # list of tuples with the correct values
        expected_values = [("MATH166", 7),
                           ("MATH166", 999),
                           ("CS222", 222),
                           ("ENG103", 28)]
        for i in range(4):
            correct = expected_values[i]
            self.assertEqual(results[i], correct)

        # test bad input
        with self.assertRaises(Exception):
            # 1"o"1 
            bad_entry = ["MATH166", "1o1", "MWF", "1100", "1345"]
            view_courses.sort_key(Course(*bad_entry))

    def test_sort_courses(self):
        expected_output = {
            'CS120': [
                Course('CS120', '1', 'MWF', '1000', '1050'),
                Course('CS120', '10', 'MWF', '0900', '0950')
            ],
            'MATH166': [
                Course('MATH166', '5', 'TR', '1100', '1215')
            ]
        }

        result = view_courses.sort_courses(TEST_TEXT_CONTENT)
        self.assertEqual(result, expected_output)

    def test_sort_courses_with_duplicates(self):
        duplicate_content = [
            "CS120\t10\tMWF\t0900\t0950\n",
            "CS120\t10\tMWF\t0900\t0950\n",
            "CS120\t10\tMWF\t0900\t0950\n",
            "CS120\t1\tMWF\t1000\t1050\n",
            "MATH166\t5\tTR\t1100\t1215\n",
            "MATH166\t5\tTR\t1100\t1215\n"
        ]

        expected_output = {
            'CS120': [
                Course('CS120', '1', 'MWF', '1000', '1050'),
                Course('CS120', '10', 'MWF', '0900', '0950')
            ],
            'MATH166': [
                Course('MATH166', '5', 'TR', '1100', '1215')
            ]
        }

        result = view_courses.sort_courses(duplicate_content)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
