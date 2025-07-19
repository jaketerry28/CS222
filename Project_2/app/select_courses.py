# select_courses.py

def get_course_count_from_user(max_courses: int) -> int:
    """
    Prompts user to specify how many courses to register for.
    Ensures input is a valid integer between 1 and max_courses.
    """
    while True:
        try:
            count = int(input(f"How many courses would you like to register for? (1 - {max_courses}): "))
            if 1 <= count <= max_courses:
                return count
            else:
                print(f"Please enter a number between 1 and {max_courses}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

