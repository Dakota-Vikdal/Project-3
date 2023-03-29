from db.models import ProjectGroup, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.project_group = [group for group in session.query(ProjectGroup)]
        self.student = [student for student in session.query(Student)]
        self.name = user_input
        self.start()
    
    def start(self):
        print(' ')
        print(f'** Welcome To C L I-din {self.name} ***')
        print(' ')

        exit = False
        while exit == False:
                choice = input(f'Type "list" to see the Full List of Students or Project Groups, type "add" to add a Student or Project Group, type "search" to Search by Student or Project Group: ')
                print(' ') 
                if choice.lower() == "list":
                     show_data(self)
                elif choice.lower() == "add":
                     add_data(self)
                elif choice.lower() == "search":
                     search_data(self)
        
                print(' ')
                user_input = input("Would you like to stop now? (Type Y/N): ")
                print(' ')
                if user_input == "Y" or user_input == 'y':
                    exit = True

        printer(self.name)

def show_data(self):
    user_action = input("Type PG to list Project Groups, S to list Students: ")
    print(' ')
    if user_action == "PG" or user_action == "pg" or user_action == "Pg":
        print_project_groups(self.project_group)
    elif user_action == "S" or user_action == "s":
        print_students(self.student)
    # elif user_action == "B" or user_action == "b":
    #     print_bottles(self.bottles)

def add_data(self):
    user_action = input("Type PG to add a Project Group or S to add a Student: ")
    print(' ')

    if user_action == "pg" or user_action == "PG":
        name = input("Type project group name: ")
        projectgroup = ProjectGroup(name = name)

        session.add(projectgroup)
        session.commit()

        self.project_group.append(projectgroup)

    elif user_action == "S" or user_action == "s":
        print_project_groups(self.project_group)
        print(' ')
        user_input = input("Is your Project Group in the list above? (Type Y/N): ")
        print(' ')

        while user_input != "Y" and user_input != "y":
            add_data(self)
            print(' ')
            print_project_groups(self.project_group)
            print(' ')
            user_input = input("Is your Project Group in the lists above? (Type Y/N): ")
            print(' ')

        make_student(self)

def make_student(self):
    user_project_group = input("Type the number of the project group from the list above: ")
    name = input("What is the student's name?: " )
    linkedin = input("What is the student's LinkedIn URL?: " )

    student = Student(
        name = name,
        linkedin = linkedin,
        project_groups_id = self.project_group[int(user_project_group) - 1].id,
)

    session.add(student)
    session.commit()

    self.student.append(student)
    print(' ')
    print('Congratulations! You have added the following student to your Project Group!')

    print_student(student)

def search_data(self):
    user_action = input("Type PG to search Project Groups or S to search Students: ")
    print(' ')
    if user_action == "PG" or user_action == "pg" or user_action == "Pg":
        print_project_groups(self.project_group)
        user_pick = input("Type the number of the Project Group from the list above to see more information: ")
        print('')
        print_project_group(self.project_group[int(user_pick) -1])
    elif user_action == "S" or user_action == "s":
        print_students(self.student)
        user_pick = input("Type the number of the Student from the list above to see more information: ")
        print(' ')
        print_student_details(self.student[int(user_pick) - 1])

def print_project_groups(groups):
    print(' ')
    print('Project Groups')
    print(' ')

    for index, group in enumerate(groups):
        print(f'{index + 1}. {group.name}')
    
    print(' ')

def print_project_group(ProjectGroup):
    print('')
    print(f'Project Group ID: {ProjectGroup.id}')
    print(f'    Project Group Name: {ProjectGroup.name}')
    print(f'    Project Group Students: {ProjectGroup.students}')

def print_students(students):
    print(' ')
    print('Students')
    print(' ')

    for index, student in enumerate(students):
        print_student(student)
    print(' ')  

def print_student(student):
    print(' ')
    print(f'Student ID: {student.id}')
    print(f'    Student Name: {student.name}')

def print_student_details(student):
    print('')
    print(f'Group ID: {student.project_groups_id}')
    print(f'    Student Name: {student.name}')
    print(f'    Student LinkedIn: {student.linkedin}')

def printer(user_input):
    print(' ')
    print(f'Goodbye {user_input}!')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/pg-to-students.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)
