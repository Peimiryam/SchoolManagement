#variables
type_of_user = ["student", "teacher", "homeroomteacher"]
commands = ["create", "manage", "end"]

#student class creation
class Student:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.classname = input ("Enter your class: ")
      
#teacher class creation
class Teacher:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.subject = input("Enter your Subject: ")
        self.classes = input("Enter your classes: ") 

#homeroom class creation
class Homeroomteacher:
    def __init__(self):

        self.name = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.classname = input ("Enter your classes: ") 
    
#menu intro
print ("Hello, welcome to the school management program.\n ")
class Menu:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.homeroomteachers = []

    def student_creation(self):
        student = Student()
        self.students.append(student)
        print("Student created")

    def teacher_creation(self):
        teacher = Teacher()
        self.teachers.append(teacher)
        print("Teacher created")

    def homeroom_teacher_creation(self):
        homeroomteacher = Homeroomteacher()
        self.homeroomteachers.append(homeroomteacher)
        print("Homeroomteacher created")

#user type creation
    def user_creation(self):
        user = input("Enter the user type: student, teacher, homeroomteacher: ")
        user = user.lower()
        if user == "student":
            self.student_creation()
        if user not in type_of_user:
            print("Wrong input")
            return
        if user == "teacher":
            self.teacher_creation()
        if user == "homeroomteacher":
            self.homeroom_teacher_creation()
        if user == "end":
            return
        
#manage menu
    def manage(self):
        manage = input("Select the user type: student, teacher, homeroomteacher: ")

        if manage not in type_of_user:
            print("Wrong input")
            return
        if manage == "student":
            student_name = input("Enter your name: ")
            for student in self.students:
                if student_name == student.name:
                    print(f"user card:\n Name: {student.name}\n Surname: {student.surname}\n Classname: {student.classname}.")            
        if manage == "teacher":
            teacher_name = input("Enter your name: ")
            for teacher in self.teachers:
                if teacher_name == teacher.name:
                    print(f"user card:\n Name: {teacher.name}\n Surname: {teacher.surname}\n Subject: {teacher.subject}\n. Classes: {teacher.classes}.")
        if manage == "homeroomteacher":
            homeroomteacher_name = input("Enter your name: ")
            for homeroomteacher in self.homeroomteachers:
                if homeroomteacher_name == homeroomteacher.name:
                    print(f"user card:\n Name: {homeroomteacher.name}\n Surname: {homeroomteacher.surname}\n Classname: {homeroomteacher.classname}.")
                    for student in self.students:
                        if homeroomteacher.classname == student.classname:
                            print(f"Student: {student.name}{student.surname}")

menu = Menu()
while True:
    command = input ("Enter one of the command: create, manage, end:")
    if command not in commands:
        print("Please enter a valid command: ")
        continue
    if command == "create":
        menu.user_creation()
    if command == "manage":
        menu.manage()
    if command == "end":
        print("Goodbye!")
        break