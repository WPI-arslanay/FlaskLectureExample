from app import app,db
from app.models import Course

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Course': Course}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)