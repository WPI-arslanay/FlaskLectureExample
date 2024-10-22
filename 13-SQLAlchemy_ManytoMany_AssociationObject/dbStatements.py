from app import app
from app import db
from app.models import Course, Room, TeachingAssistant, TA_Assignment
import sqlalchemy as sqla

app.app_context().push()
db.create_all()


# create Room and write it to DB
newroom = Room(building='Fuller',roomNumber='PHU', capacity=100)
db.session.add(newroom)
db.session.commit()

# create Course and write it to DB
newCourse = Course(major='CS',coursenum='3733', title='Software Engineering', roomid = newroom.id, type = 1)
db.session.add(newCourse)
newCourse = Course(major='CS',coursenum='1102', title='Programming with Gregor!', roomid = newroom.id, type = 2)
db.session.add(newCourse)
db.session.commit()


# create a TA and write it to DB
newTA = TeachingAssistant(ta_name = 'Guangbei')
db.session.add(newTA)
db.session.commit()

# get the Course object for CS 3733
thecourse = db.session.scalars(sqla.select(Course).where(Course.major == 'CS').where(Course.coursenum == '3733')).first()

#create a new TA_Assignment
newTAship = TA_Assignment(course_id = thecourse.id, ta_id = newTA.id)  #not providing the assign date, will use default value
db.session.add(newTAship)
db.session.commit()

# add newTAship as a new assignment for thecourse
# thecourse.ta_positions.add(newTAship)

#check the course and teaching assistant of the newTAship
print(newTAship.course_assigned)
print(newTAship.ta_assigned)

# check the TAships of the course
print(db.session.scalars(thecourse.ta_positions.select()).all())

#check the TAships of the TA
print(db.session.scalars(newTA.taships.select()).all())

