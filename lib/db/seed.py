from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import ProjectGroup, Student

if __name__ == '__main__':
    engine = create_engine('sqlite:///pg-to-students.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(ProjectGroup).delete()
    session.query(Student).delete()

    fake = Faker()

    linkedin = ['abc', 'def', 'ghi',
        'jkl', 'mno', 'pqr', 'tuv', 'wx', 'yz']
    # platforms = ['nintendo 64', 'gamecube', 'wii', 'wii u', 'switch',
    #     'playstation', 'playstation 2', 'playstation 3', 'playstation 4',
    #     'playstation 5', 'xbox', 'xbox 360', 'xbox one', 'pc']

    projectgroups = []
    for i in range(10):
        projectgroup = ProjectGroup(
            name=fake.unique.name()
        )

        # add and commit individually to get IDs back
        session.add(projectgroup)
        session.commit()

        projectgroups.append(projectgroup)

    students = []
    for projectgroup in projectgroups:
        for i in range(3,4):
            student = Student(
                name=fake.unique.name(),
                linkedin=random.choice(linkedin),
                project_groups_id = projectgroup.id
            )

            students.append(student)
    
    session.bulk_save_objects(students)
    session.commit()
    session.close()