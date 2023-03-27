from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class ProjectGroup(Base):
    __tablename__ = 'project_groups'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    students = relationship('Student', backref=backref('student'))

    def __repr__(self):
        return f'ProjectGroup(id={self.id}, ' + \
            f'name={self.name})'

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(Integer())
    linkedin = Column(String())

    project_groups_id = Column(Integer(), ForeignKey('project_groups.id'))

    def __repr__(self):
        return f'Student(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'linkedin={self.linkedin})'