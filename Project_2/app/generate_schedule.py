# generate_schedule.py
# generate a schedule with backtracking
    
def generate_schedule(schedule, selected_courses, courses_available):

    # base case
    # schedule contains valid sections for all registered courses
    if len(schedule) == len(selected_courses):
        return schedule
    
    # find the first unassigned course, look at all sections
    course_name = selected_courses[len(schedule)]

    # check for overlaps in course sections to already assigned sections
    for section in courses_available[course_name]:
        # if all return false
        if all(not section.check_for_overlaps(schedule[already_assigned]) for already_assigned in schedule):
               
               # temporary add course and section to the schedule 
               schedule[course_name] = section
               
               # backtracking
               # if basecase is met, returns schedule
               result = generate_schedule(schedule, selected_courses, courses_available)
               if result:
                    return result
               
               # if no basecase, delete course and try next
               del schedule[course_name]
    
    return None