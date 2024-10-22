
from app import app
from app import db
from app.models import Course, Room
import sqlalchemy as sqla

app.app_context().push()
db.create_all()

# create Room and write it to DB
newroom = Room(building='Fuller',roomNumber='PHU', capacity=100)
db.session.add(newroom)
db.session.commit()

# query the classes for a room
theroom = Room.query.filter_by(id=1).first()
theroom = Room.query.filter_by(building = 'Fuller').filter_by(roomNumber = 'PHU').first()


# create Course and write it to DB
newCourse = Course(major='CS',coursenum='3733', title='Software Engineering', roomid = theroom.id)
db.session.add(newCourse)
newCourse = Course(major='CS',coursenum='1102', title='Programming with Gregor!', roomid = theroom.id)
db.session.add(newCourse)
db.session.commit()

cs_courses  = db.session.scalars(sqla.select(Course).where(Course.major == 'CS')).all()
first_cs_course  = db.session.scalars(sqla.select(Course).where(Course.major == 'CS')).first()
sorted_cs_courses  = db.session.scalars(sqla.select(Course).where(Course.major == 'CS').order_by(Course.title)).all()
cs_courses_count = db.session.scalar(sqla.select(db.func.count()).where(Course.major == 'CS'))

# get the room for CS 3733
thecourse = db.session.scalars(sqla.select(Course).where(Course.major == 'CS' and Course.coursenum == '3733')).first()
thecourse = db.session.scalars(sqla.select(Course).where(Course.major == 'CS').where(Course.coursenum == '3733')).first()
thecourse.classroom

#query for a room
theroom = db.session.scalars(sqla.select(Room).where(Room.building == 'Fuller').where(Room.roomNumber == 'PHU')).first()
db.session.scalars(theroom.courses.select()).all()


