import os
from dynaconf import FlaskDynaconf

HERE = os.path.dirname(os.path.abspath(__file__))


def configure(app):
    """\
    Configure the application with Dynaconf.
    """
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=HERE)
