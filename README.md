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
- [x] Extensions and CLI
    - Flask Script for commands like `runserver` and `shell`
- [x] Databases (Relational) with Postgres
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


##  Resources
**N/B** I may not have looked at many of this resources, so if some contain incorrect/outdated info am not to blame, you should refer to multiple sources.
### Flaskhttps://blog.tecladocode.com/learn-python-password-encryption-with-flask/
- [Official Flask Documentation](https://flask.palletsprojects.com/)
- [Miguel blog](https://blog.miguelgrinberg.com/category/Flask)
    - [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    
### Postgres 
- [https://www.postgresqltutorial.com/](https://www.postgresqltutorial.com/)
- [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)

### Extensions
- [https://flask.palletsprojects.com/en/1.1.x/extensions/](https://flask.palletsprojects.com/en/1.1.x/extensions/)

### Flask Script & Flask In Built CLI tool
- [Flask Script](https://flask-script.readthedocs.io/en/latest/)
- [https://flask.palletsprojects.com/en/1.1.x/cli/](https://flask.palletsprojects.com/en/1.1.x/cli/)

### Sqlalchemy
- [https://flask-sqlalchemy.palletsprojects.com/](https://flask-sqlalchemy.palletsprojects.com/)
- [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)
- [https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

### Database Migrations with Alembic & Flask Migrate
- [https://flask-migrate.readthedocs.io/en/latest/](https://flask-migrate.readthedocs.io/en/latest/)
- [https://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask](https://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask)
- [Flask Alembic](https://flask-alembic.readthedocs.io/en/stable/)
- [https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)

### Python Dotenv
- [https://saurabh-kumar.com/python-dotenv/](https://saurabh-kumar.com/python-dotenv/)

### Protecting user password /Hashing
- [https://www.wired.com/2016/06/hacker-lexicon-password-hashing/](https://www.wired.com/2016/06/hacker-lexicon-password-hashing/)
- [https://auth0.com/blog/hashing-passwords-one-way-road-to-security/](https://auth0.com/blog/hashing-passwords-one-way-road-to-security/)
- [https://blog.tecladocode.com/learn-python-password-encryption-with-flask/](https://blog.tecladocode.com/learn-python-password-encryption-with-flask/)
- [https://techmonger.github.io/4/secure-passwords-werkzeug/](https://techmonger.github.io/4/secure-passwords-werkzeug/)
