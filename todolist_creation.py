from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/123'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db = SQLAlchemy(app)


class todolist(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.INT, primary_key=True)
    title = db.Column(db.VARCHAR(100))
    content = db.Column(db.VARCHAR(255))
    completion_status = db.Column(db.VARCHAR(10))
    add_time = db.Column(db.INT)
    deadline = db.Column(db.INT)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
