from app import db

import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

class Room(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    building : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(50)) 
    roomNumber : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))   
    capacity : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer)
    #relationships
    courses : sqlo.WriteOnlyMapped['Course'] = sqlo.relationship(back_populates= 'classroom')
    
    def __repr__(self):
        return '<Room {},{},{},{} >'.format(self.id, self.building, self.roomNumber, self.capacity)
    
assigned = db.Table(
    'assigned',
    db.metadata,
    sqla.Column('course_id', sqla.Integer, sqla.ForeignKey('course.id'), primary_key= True),
    sqla.Column('ta_id', sqla.Integer, sqla.ForeignKey('teachingassistant.id'), primary_key= True)
)

class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    roomid : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Room.id))
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    major : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))
    #relationships
    classroom : sqlo.Mapped[Room] = sqlo.relationship( back_populates= 'courses')
    tas : sqlo.WriteOnlyMapped['TeachingAssistant'] = sqlo.relationship(
        secondary= assigned,
        primaryjoin= (assigned.c.course_id == id),
        back_populates= 'courses')
    
    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
    
    def add_ta(self,new_ta):
        if not self.is_ta(new_ta):
            self.tas.add(new_ta)

    def is_ta(self,new_ta):
        result = db.session.scalars(self.tas.select().where(assigned.c.ta_id == new_ta.id)).first()
        return result is not None

    def all_tas(self):
        return db.session.scalars(self.tas.select()).all()

class TeachingAssistant(db.Model):
    __tablename__ = 'teachingassistant'
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    ta_name : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(100))
    # relationships
    courses : sqlo.WriteOnlyMapped['Course'] = sqlo.relationship(
        secondary= assigned,
        primaryjoin= (assigned.c.ta_id == id),
        back_populates= 'tas')
    
    def __repr__(self):
        return '<TA {} - {};>'.format(self.id,self.ta_name)

