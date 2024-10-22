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
    

class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    roomid : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(Room.id))
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    major : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))
    #relationships
    classroom : sqlo.Mapped[Room] = sqlo.relationship( back_populates= 'courses')

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
