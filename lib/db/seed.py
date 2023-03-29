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

    linkedin = ['studenta@linkedin.com', 'studentb@linkedin.com', 'studentc@linkedin.com',
        'studentd@linkedin.com', 'studente@linkedin.com', 'studentf@linkedin.com', 'studentg@linkedin.com', 'studenth@linkedin.com', 'studenti@linkedin.com', 'studentj@linkedin.com']
    groupnames = ['nintendo 64', 'gamecube', 'switch',
        'playstation', 'playstation 2', 'playstation 3', 'xbox', 'xbox 360', 'xbox one', 'pc']

    projectgroups = []
    for i in range(10):
        projectgroup = ProjectGroup(
            name=random.choice(groupnames)
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