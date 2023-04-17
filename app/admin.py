from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .import models

session = models.db.session

admin = Admin()
admin.add_view(ModelView(models.User, session))
# admin.add_view(ModelView(models.StudyGroup, session))
# admin.add_view(ModelView(models.Teacher, session))
# admin.add_view(ModelView(models.Room, session))
# admin.add_view(ModelView(models.Lesson, session))
