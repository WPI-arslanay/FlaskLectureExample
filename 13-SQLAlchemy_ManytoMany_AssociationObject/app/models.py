from app import db
from datetime import datetime, timezone
from typing import Optional
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

class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    roomid : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Room.id))
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    major : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))
    type : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer)
    #relationships
    classroom : sqlo.Mapped[Room] = sqlo.relationship( back_populates= 'courses')
    ta_positions : sqlo.WriteOnlyMapped['TA_Assignment'] = sqlo.relationship( back_populates= 'course_assigned' )
   
    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
    
    def add_ta(self,new_ta):
        if not self.is_ta(new_ta):
            new_assignment = TA_Assignment( ta_assigned = new_ta)
            self.ta_positions.add(new_assignment)
            db.session.commit()

    def is_ta(self,new_ta):
        result = db.session.scalars(self.ta_positions.select().where(TA_Assignment.ta_id == new_ta.id)).first()
        return result is not None

    def all_tas(self):
        # returns a list of TA_assignment objects
        return db.session.scalars(self.ta_positions.select()).all()
    
    def get_assignment_date(self, the_ta):
        if self.is_ta(the_ta):
            return db.session.scalars(sqla.select(TA_Assignment).where(TA_Assignment.course_id == self.id).where(TA_Assignment.ta_id == the_ta.id)).first().assign_date
        else:
            return None 
    
class TeachingAssistant(db.Model):
    __tablename__ = 'teachingassistant'
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    ta_name : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(100))
    # relationships
    taships : sqlo.WriteOnlyMapped['TA_Assignment'] = sqlo.relationship(back_populates= 'ta_assigned')   
    def __repr__(self):
        return '<TA {} - {};>'.format(self.id,self.ta_name)


class TA_Assignment(db.Model):
    course_id : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Course.id), primary_key=True)
    ta_id : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(TeachingAssistant.id), primary_key=True)
    assign_date : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column(default = lambda : datetime.now(timezone.utc))
    course_assigned : sqlo.Mapped[Course] = sqlo.relationship(back_populates= 'ta_positions' )
    ta_assigned : sqlo.Mapped[TeachingAssistant] = sqlo.relationship(back_populates= 'taships' )

    def __repr__(self):
        return '<TA_Assignment ta: {} course: {} date: {}>'.format(self.ta_assigned,self.course_assigned, self.assign_date)