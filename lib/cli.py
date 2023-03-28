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
                choice = input(f'Type "list" to see the Full List of Student and their LinkedIns, type "add" to add a Student or LinkedIN Profile, type "search" to Search by Student: ')
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
    user_action = input("Type B to add a bottle, G to add a grape or W to add a winery: ")
    print(' ')

def search_data(self):
     pass

def print_project_groups(groups):
    print(' ')
    print('Project Groups')
    print(' ')

    for index, group in enumerate(groups):
        print(f'{index + 1}. {group.name}')
    
    print(' ')

def print_students(students):
    print(' ')
    print('Students')
    print(' ')

    for index, student in enumerate(students):
        print_student(student)
    print(' ')  

def print_student(student):
    print(' ')
    print(f'Group ID: {student.project_groups_id}')
    # print(f'Grape: {bottle.grape.name}')
    print(f'    Student Name:{student.name}')
    print(f'    Student LinkedIn: {student.linkedin}')
    # print(f'    Score: {bottle.score}')

def printer(user_input):
    print(' ')
    print(f'Goodbye {user_input}!')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/pg-to-students.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Your Name: ")
    CLI(user_input)
