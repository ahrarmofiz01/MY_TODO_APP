from app import db
class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.string(100),nullable=False)
    status = db.column(db.string(20),defalult="pending")