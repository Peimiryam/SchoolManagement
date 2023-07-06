type_user = ["student", "teacher", "homeroomteacher", "end"]

commands = ['create', 'manage', 'end']

database = {}

students = []
teachers = []
homeroomteachers = []

#Main menu
def main(command):

    while True:

        command = input("Write one of the following command: 'create' 'manage' 'end':  ")

        if command not in commands:
            print("Invalid input. ")
            continue

        elif command == 'create':
            create(type_user)
            
        elif command == 'manage':
            manage_members()

        elif command == 'end':
            print("Have a nice day. Goodbye! ")
        break

#user creation
def create(type_user):
    type_user = input("Select the type of user: 'student' 'teacher' 'homeroom teacher'\n or input 'end' to return to the main menu: ")

    if type_user not in type_user:
         print("Wrong input. ")

    elif type_user == 'student':
            print("Student creation in progress: ")
            student_creation()
        
    elif type_user == 'teacher':
            print("teacher creation in progress")
            teacher_creation()

    elif type_user == 'homeroom teacher':
            print("homeroom teacher creation in progress")
            homeroom_creation()
        
    elif type_user == "end":
        main(commands)

#student creation
def student_creation():

    name = input("Insert a name and surname: ")
    classes = input("Insert a class: ")
    students.append(name)
    students.append(classes)
    database[name]=[f"Name/Surname: {name} , Class: {classes}"]
    print(students)
    main(commands)
        
#teacher creation
def teacher_creation():
    name = input("Insert a name and surname: ")
    classes = input("Insert a class: ")
    subject = input("Insert a subject: ")
    teachers.append(name)
    teachers.append(classes)
    teachers.append(subject)
    database[name]=[f"Name/Surname: {name}, Class: {classes}, Subject: {subject}"]
    print(teachers)
    main(commands)

def homeroom_creation():
    name = input("Insert a name and surname: ")
    classes = input("Insert a class: ")
    homeroomteachers.append(name)
    homeroomteachers.append(classes)
    database[name]=[f"Name/Surname: {name}, Classes: {classes}"]
    print(homeroomteachers)
    main(commands)

#search and get values
def manage_members():
    manage = input("Select the field to edit: student, teacher, homeroomteacher: ")

    if manage not in type_user:
         print("Wrong input")

    elif manage == "student":
        search = input("Insert the name and surname you want to search: ")
        if search in database:
            print(database[search])
        else:
             print("Not available")
        main(commands)

    elif manage == "teacher":
        search = input("Insert the name you want to search: ")
        if search in database:
            print(database[search])
        else:
             print("Not available")
        main(commands)

    elif manage == "homeroomteacher":
        search = input("Insert the name you want to search: ")
        if search in database:
            print(database[search])
        else:
             print("Not available")
        main(commands)

    elif manage == 'end':
         main(commands)


#main menu
print("Hello! Welcome to the School Management Software.\n ")
main(commands)