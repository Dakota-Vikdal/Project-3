from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import ProjectGroup, Student

if __name__ == '__main__':
    engine = create_engine('sqlite:///pg-to-students.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
