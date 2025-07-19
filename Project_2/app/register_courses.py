from app.view_courses import display_available_courses

def register_for_courses(offered_courses, n_courses, registered_courses):
    i = 0
    while i < n_courses:

        if registered_courses:
            print("Registered courses:")
            for course in registered_courses:
                print(course)  

        # get user input
        display_available_courses(offered_courses)
        course_id = input("\nEnter the Course ID or 'q' to quit: ").upper()
        if course_id == 'Q':
            print("\nExiting course registration.")
            return registered_courses
        
        # validate course exists
        if course_id != 'Q' and course_id not in offered_courses:
            print(f"\nThat course does not exist.")
            continue        

        # check if already registered
        already_registered = False
        for course in registered_courses:
            if course == course_id:
                print("\nAlready registered for that course. Please choose a different one.")
                already_registered = True
                break

        # go to start of loop to let user select another course    
        if already_registered:
            continue

        # append course id to list
        registered_courses.append(course_id)

        i += 1      
    
    if registered_courses:
        print("Registered courses:")
        for course in registered_courses:
            print(course)
                     
    return registered_courses

