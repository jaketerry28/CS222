# main.py

from app.view_courses import *
from app.select_courses import get_course_count_from_user
from app.register_courses import register_for_courses
from app.generate_schedule import *

def menu():
    print("0) Exit")
    print("1) View Available Courses")
    print("2) Select Courses to Register")
    print("3) Generate Course Schedule")
    response = input("Select an option: ")
    if response in ['0', '1', '2', '3']:
        return response
    else:
        print("\nPlease enter a valid option 0-3.")

def start(courses_file):
    # Initialize an empty list to hold registered courses
    selected_courses = []  

    # Initialize a variable to keep track of the number of courses to register
    # Default to 1 course if not specified by the user
    course_count = 1

    # Load and sort the courses from the file
    course_list = get_courses(courses_file)
    offered_courses = sort_courses(course_list)

    # Main loop for the course scheduler
    keep_going = True
    print("Welcome to the Course Scheduler!")
    while keep_going:
        choice = menu()

        if choice == '0':
            print("Exiting the Course Scheduler. Goodbye!")
            keep_going = False

        elif choice == '1':
            print("\nHere are the courses offered this semester:")
            see_all_courses(offered_courses)

        elif choice == '2':
            # Initialize an empty list to hold registered courses
            selected_courses = []            
            course_count = get_course_count_from_user(max_courses=len(offered_courses))
            print(f"\nYou chose to register for {course_count} course(s).")
            register_for_courses(offered_courses, course_count, selected_courses)

        elif choice == '3':
            if not selected_courses:
                print("\nYou have not registered for any courses yet.")
            else:
                print("\nYour Course Schedule\n")
                print("================================================")
                schedule = generate_schedule({}, selected_courses, offered_courses)
                if schedule:
                    for course in schedule:
                        print(str(schedule[course]))
                else:
                    print("No valid schedules can be made.")

def main():
    start("source/courses1.txt")
    

if __name__ == "__main__":
    main()
