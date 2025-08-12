from flask import Flask
from blog.config import configure


def create_app():
    """\
    Main Factory
    
    Create the instance of app and delegate to another function to 
    configure it and return an app running.
    """
    app = Flask(__name__)
    configure(app)
    return app
