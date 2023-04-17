from flask import Flask

from .admin import admin
from .models import db, migrate
from . import views


def create_app(config=None):
    app = Flask(__name__)

    # Конфигурация
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    if config:
        app.config.from_mapping(config)

    # База данных
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    admin.init_app(app)

    # Функции представления
    app.add_url_rule("/", view_func=views.index_page)

    return app
