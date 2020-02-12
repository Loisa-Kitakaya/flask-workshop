from flask_script import Command

class HelloWorldCommand(Command):

    def run(self):
        print("Hello world")