from app import app,db
from app.models import Course, Room
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Course': Course, 'Room': Room }


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)