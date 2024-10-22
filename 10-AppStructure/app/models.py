from app import db
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    major : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
