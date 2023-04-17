from flask import render_template
from .models import db


def index_page():
    # query = db.select(Student).order_by("last_name", "first_name", "second_name")
    # result = db.session.execute(query).scalars()
    return render_template("index.html")
