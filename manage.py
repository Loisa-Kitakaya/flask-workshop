from app import create_app,db
from app.models import User,Device
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.commands.hello_world import HelloWorldCommand

app = create_app()
manager = Manager(app)
manager.add_command("runserver",Server(use_debugger=True))
migrate = Migrate(app,db)
manager.add_command("db",MigrateCommand)
manager.add_command("hw",HelloWorldCommand)

@manager.shell
def add_context():
    return {"db":db,"app":app}
if __name__=="__main__":
    manager.run()