from db.models import ProjectGroup, Student
from project_group import print_project_group, print_project_groups
from students import print_students, print_student_details
# from cli import session

def show_data(self):
    user_action = input("Type PG to list Project Groups, S to list Students: ")
    print(' ')
    if user_action == "PG" or user_action == "pg" or user_action == "Pg":
        print_project_groups(self.project_group)
    elif user_action == "S" or user_action == "s":
        print_students(self.student)


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
