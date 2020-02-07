# Flask Talk (WIP)
- A quickstart to flask

## TODO
- [x] Hello world Flask
    - A bit about WSGI
    - views and routing
    - running the development server(with debug mode)
- [x] Templates (jinja)
    - rendering template and passing context to template
    - tags
    - control flow(condition and loops)
    - macros
    - template inheritances
- [x] Project structure using Blueprints
- [x] Deploying to production(Heroku)
    - gunicorn as our WSGI production server
- [ ] Extensions and CLI
    - Flask Script for commands like `runserver` and `shell`
- [ ] Databases (Relational) with Postgres
    - CRUD
    - Relationships
    - SQLAlchemy models and relationships (ORM)
    - DB Migrations using alembic
- [ ] Authentication with Flask-Login
- [ ] Testing our Flask app
- [ ] Misc
    - Sending Mails
    - CSRF protection


## Setup 
- Use python3
### Clone
`git clone https://github.com/jakhax/flask-workshop.git`
### Create virtual
There are many ways to create a virtual env i use:
```bash
python3 -m venv virtual
```
Activate virtual and install requirements
```bash
# for unix users
source virtual/bin/activate
pip install - requirements.txt
```
### run server
- Development server `python manage.py`
- Production server `gunicorn "manage:app"`


## Recommended resources
- [Official Flask Documentation](https://flask.palletsprojects.com/)