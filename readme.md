# Flask-5

## Предварительные шаги

1. Откройте каталог проекта в редакторе VS Code

2. Создайте и активируйте виртуальное окружение 

Powershell:

```powershell
py -m venv venv
.\venv\scripts\activate.ps1
```

Командная строка:

```cmd
py -m venv venv
venv\scripts\activate.bat
```

3. Установите библиотеки используя список из `requirements.txt`:

```powershell
pip install -r requirements.txt
```

4. Инициализируйте базу данных:

```powershell
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Разрешите отладку и запустите веб-сервер разработчика:

Powershell:

```powershell
$ENV:FLASK_DEBUG=1
flask run
```

Командная строка:

```cmd
set FLASK_DEBUG=1
flask run
```

## Работа с формами

Проверьте работу

Сделайте коммит

## Модульное тестирование

Проверьте работу

Сделайте коммит

## Публикация на хостинге

1. Создайте бесплатный аккаунт на сайте [PythonAnywhere](https://www.pythonanywhere.com)

2. 

Проверьте работу

## Ссылки

* [Документация Flask](https://flask.palletsprojects.com/)
* [Документация Flask-WTF](https://flask-wtf.readthedocs.io/)
* [Документация Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [Документация Flask-Migrate](https://flask.palletsprojects.com/)
* [Документация Flask-Admin](https://flask-admin.readthedocs.io/)
* [Документация WTForms](https://wtforms.readthedocs.io/)
* [Документация SqlAlchemy](https://www.sqlalchemy.org/)
* [Документация Alembic](https://alembic.sqlalchemy.org/)
