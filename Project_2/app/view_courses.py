### view_courses.py
from app.Course import Course

def sort_key(course_obj):
    # get course name, and course section for sorting
    if not course_obj.section.isdigit():
        raise Exception(f"Section {course_obj.section} is invalid.")
    else:
        return (course_obj.course_id, int(course_obj.section))

def get_courses(courses_file):
    try:
        with open(courses_file, 'r') as file:
            course_list = file.readlines()
            return course_list
    except:
        raise FileNotFoundError(f"Error: {courses_file} not found.")

def sort_courses(course_list):
    # create a dictionary to hold courses
    # where the key is the course name and the value is a list of Course objects
    course_dict = {}
    for line in course_list:
        course_data = line.strip().split('\t')
        course_obj = Course(*course_data)
        course_name = course_obj.course_id

        if  course_name not in course_dict:
            course_dict[course_name] = []

        if course_obj not in course_dict[course_name]:
            course_dict[course_name].append(course_obj)

    # sort each course's list of sections
    for course_id in course_dict:
        course_dict[course_id].sort(key=sort_key)

    return course_dict

def see_all_courses(course_dict):
    for course_id in sorted(course_dict):
        for section in course_dict[course_id]:
            print(section)


def display_available_courses(course_dict):
    print("\nAvailable Courses:\n")
    for course_id, sections in course_dict.items():
        print(f"{course_id}: {len(sections)} section(s)")

