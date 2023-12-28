
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///models.db')

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__='auditions'
    id= Column(Integer(), primary_key=True)
    actor= Column(String())
    location= Column(String())
    phone=Column(Integer())
    hired=Column(Boolean())
    role_id= Column(Integer())

    def call_back(self):
        self.hired = True

    def __repr__(self):
        return f'<Auditions {self.actor}>' \
            + f'{self.location}'\
            + f'{self.phone}' \
            + f'{self.phone}' \
            + f'{self.hired}' \
            + f'{self.role_id}'
    
class Role(Base):
    __tablename__='roles'
    id= Column(Integer(), primary_key=True)
    character_name= Column(String())

    auditions = relationship('Audition')

    def actors(self):
        return [audition.actor for audition in self.auditions]
    def location(self):
        return [audition.location for audition in self.audition]
    def lead(self):
        hired_auditions = [audition for audition in self.audition if audition.hired]
        if hired_auditions:
            return hired_auditions[0]
        else:
            return 'no actor has been hired for this role'
    def understudy(self):
        hired_auditions=[audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) >= 2:
            return hired_auditions[1]
        else:
            return 'no actor has been hired for understudy for this role'

    def __repr__(self):
        return f'<Roles {self.character_name}>'
