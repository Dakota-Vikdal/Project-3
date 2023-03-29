from db.models import ProjectGroup, Student



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