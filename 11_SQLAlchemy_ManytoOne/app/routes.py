from __future__ import print_function
import sys
from flask import render_template, flash, redirect, url_for, request

from app import app,db
from app.forms import CourseForm
from app.models import Course, Room
import sqlalchemy as sqla

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()
        # create the rooms 
        allrooms = [{'building' : 'Fuller', 'roomNumber' : 'PHU', 'capacity' : 60}, 
                    {'building' : 'UnityHall', 'roomNumber' : '175', 'capacity' : 100},
                    {'building' : 'UnityHall', 'roomNumber' : '150', 'capacity' : 80}]
        if len(db.session.scalars(sqla.select(Room)).all()) == 0:
            for room in allrooms:
                theroom = Room (building = room['building'],roomNumber=room['roomNumber'], capacity = room['capacity'] ) 
                db.session.add(theroom)
                db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():  
    form = CourseForm()
    if form.validate_on_submit():
        if (form.major.data is not None) and (form.coursenum.data is not None):
            #check if course already exists
            course_count = db.session.scalar(sqla.select(db.func.count()).where(Course.major == form.major.data).where(Course.coursenum == form.coursenum.data))
            if course_count < 1:
                newcourse = Course(major = form.major.data,coursenum = form.coursenum.data,title = form.title.data, roomid = form.classroom.data.id)
                db.session.add(newcourse)
                db.session.commit()
                return redirect(url_for('course',name="{}{}-{}".format(form.major.data,form.coursenum.data, form.title.data)))
            else:
                flash("Course {} {} already exists!".format(form.major.data,form.coursenum.data))
    # display existing courses
    all_courses = db.session.scalars(sqla.select(Course).order_by(Course.major)).all()
    return render_template('index.html', form=form, courses = all_courses)


@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)