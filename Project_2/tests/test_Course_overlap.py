import unittest
from app.Course import Course

class TestCourseOverlap(unittest.TestCase):
    
    def setUp(self):

        # overlaps exist between:
            # CS101 001, CS120 011
            # CS101 001, CS120 223
            # MATH201 002, CS120 563

        self.offered_courses = {
            "CS101": [
                Course("CS101", "001", "MWF", "0900", "0950"),
                Course("CS101", "101", "MWF", "1300", "1350")
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

    def test_overlap_between_different_courses(self):
        overlaps = []
        all_courses = list(self.offered_courses.items())

        # check for overlap between each pair
        for i in range(len(all_courses)):
            course_id_a, list_of_sections_a = all_courses[i]
            for j in range(i+1, len(all_courses)):
                course_id_b, list_of_sections_b = all_courses[j]

                # check for overlap between sections
                for sec_a in list_of_sections_a:
                    for sec_b in list_of_sections_b:
                        if sec_a.check_for_overlaps(sec_b):
                            overlaps.append((sec_a.course_id, sec_a.section, sec_b.course_id, sec_b.section))
            
        self.assertIn(('CS101', '001', 'CS120', '011'), overlaps)
        self.assertIn(('CS101', '001', 'CS120', '223'), overlaps)
        self.assertIn(('MATH201', '002', 'CS120', '563'), overlaps)
        self.assertEqual(len(overlaps), 3)




if __name__ == '__main__':
    unittest.main()
