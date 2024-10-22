import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'course.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from forms import CourseForm

class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    major : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CourseForm()
    if form.validate_on_submit():
        if (form.major.data is not None) and (form.coursenum.data is not None):
            #check if course already exists
            # course_count = db.session.scalar(sqla.select(db.func.count()).where(Course.major == form.major.data).where(Course.coursenum == form.coursenum.data))
            course_count = len( db.session.scalars(sqla.select(Course).where(Course.major == form.major.data).where(Course.coursenum == form.coursenum.data)).all())
            if course_count < 1:
                # add new course to the database
                newcourse = Course(major = form.major.data,coursenum = form.coursenum.data,title = form.title.data)
                db.session.add(newcourse)
                db.session.commit()
                return redirect(url_for('course',name="{}{}-{}".format(form.major.data,form.coursenum.data, form.title.data)))
            else:
                flash("Course {} {} already exists!".format(form.major.data,form.coursenum.data))
             
    return render_template('index.html', form=form)

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

