
# assignment3.py

# file to search
studentsFile = "students.txt" 

# convert file to dict
def fileToDictionary(studentsFile):
    try:
        studentsList = {}
        fileInput = open(studentsFile, "r")
        students = fileInput.readlines()
        fileInput.close()
        for s in students:
            parts = s.split(",")
            studentsList[parts[0]] = [parts[1], parts[2], parts[3], parts[4].rstrip('\n')]
        #print(studentsList)
        return studentsList
    except FileNotFoundError:
        print("File not found")
        return None

# menu interface
def menu(students):
    keepGoing = True
    while (keepGoing):
        print(f"Choose an option:\n1) Search by Last Name\n2) Search by Major\n3) Quit\n")
        userInput = (input("Option: "))
        if userInput == '1':
            searchStudents(students, 0, "Enter a lastName: ")
            print('\n')
        elif userInput == '2':
            searchStudents(students, 2, "Enter a Major: ")
            print('\n')
        elif userInput == '3':
            keepGoing = False
            print("Quitting")
        else:
            print("Enter a valid option.\n")

# searching
def searchStudents(students, field, menuPrompt):
    userInput = str(input(menuPrompt)).lower()
    foundStudent = False
    print("---------------------")
    for key in students:
        if students[key][field].lower() == userInput:
            res = ', '.join(students[key])
            print(f"{key}: {res}")
            foundStudent = True
    if not foundStudent:
        print("No Students Found")


def main():
    students = fileToDictionary(studentsFile)
    if students:
        menu(students)

main()