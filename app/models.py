from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(75), nullable=False)
    is_active = db.Column(db.Boolean())

    def __str__(self) -> str:
        return f"{self.name}"


# class StudyGroup(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(25), nullable=False)
#     lessons = db.relationship("Lesson", back_populates="study_group")

#     def __str__(self) -> str:
#         res = f"{self.name}"


# class Teacher(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     full_name = db.Column(db.String(75), nullable=False)
#     lessons = db.relationship("Lesson", back_populates="teacher")

#     def __str__(self) -> str:
#         res = f"{self.full_name}"


# class Room(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     number = db.Column(db.String(10), nullable=False)
#     lessons = db.relationship("Lesson", back_populates="room")

#     def __str__(self) -> str:
#         res = f"{self.number}"


# class Lesson(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     date = db.Column(db.Date(), nullable=False)
#     time = db.Column(db.Time(), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     study_group_id = db.Column(db.Integer(), db.ForeignKey("study_group.id", name="StudyGroup"))
#     study_group = db.relationship("StudyGroup", back_populates="lessons")
#     teacher_id = db.Column(db.Integer(), db.ForeignKey("teacher.id", name="Teacher"))
#     teacher = db.relationship("Teacher", back_populates="lessons")
#     room_id = db.Column(db.Integer(), db.ForeignKey("room.id", name="Room"))
#     room = db.relationship("Room", back_populates="lessons")

#     def __str__(self) -> str:
#         res = f"{self.number}"
