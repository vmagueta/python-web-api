from flask_pymongo import PyMongo

mongo = PyMongo()  # Lazy Initiation


def configure(app):
    """\
    Factory of the database extension

    Initialize the extension with the Flask application to connect in db.
    """
    mongo.init_app(app)
