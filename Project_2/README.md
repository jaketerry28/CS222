# Summer2025_Group_2

# Course scheduling application

## User Stories

Please place user stories here, so they can be collected into a pdf.

### User Story 1 - View Courses (Jake Terry)

As an student, I want to see all upcoming classes offered for the upcoming semester so that I can start planning my schedule ahead.

Acceptance criteria
 
1. The course list displays the per course:
    - Course name (e.g. CS222)
    - Section number
    - Meeting days (e.g. MWF, TH,)
    - Meeting start time (e.g. 0900)
    - Meeting end time 
2. The list is sorted alphabetically by course name.
3. If multiple courses share the same name, they are sorted by section number in ascending order.
4. The list does not show duplicate courses.

### User Story 2 - Specify Number of Courses to Register For (Zhibo Zhang)

As a student, I want to specify how many courses I want to register for, so that I can manage my course load effectively for the semester.

Acceptance Criteria The system provides an input option for students to specify the number of courses they wish to register for (e.g., a dropdown or input field).

The number entered must be a positive integer greater than zero.

If the input is invalid (e.g., negative number, zero, or non-integer), an appropriate error message is shown: "Please enter a valid number of courses."

The course registration interface adjusts to show only the number of courses the student chose.

Students can edit or update the number of courses at any time before submitting final registration.

Once submitted, the system validates that the number of selected courses does not exceed the specified amount.

A confirmation summary displays the total number of selected courses before final submission.

### User Story 3 - Register for Courses (Jake Terry)


As a student, I want to input the course numbers I want to register for so that the system can attempt to build my schedule.

Acceptance Criteria

1. The student is prompted to enter n distinct course numbers based on their previous input.

2. Course numbers are validated against the list of available courses.

3. Duplicate entries are not allowed; an error is displayed if a course is entered more than once.

=======
### User Story 4 - Remove Courses (Laney Nall)

As a student, I would like the ability to remove selected courses in case of accident.

1. If student has selected a course, then the student may prompt removal of course.

2. User is presented their currently selected courses.

3. User may type desired course to prompt deletion.

4. Course is deleted and selected courses changes to match updated version.

### User Story 5 - Generate Schedule (Laney Nall)

As a student, I want my selected courses to be generated into a schedule.

1. User may select to generate a schedule, if no courses have been selected an error message will prompt.

2. Schedule should check for overlapping courses upon generation and notify the user of said conflict and display error message.

3. If no conflict is present schedule is generated with classes.