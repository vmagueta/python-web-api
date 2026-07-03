from flask import Flask
from datetime import datetime
from mistune import markdown


def configure(app: Flask):
    # {{markdown(text)}}
    app.add_template_global(markdown)

    # {{date | format_date }}
    app.add_template_filter(lambda date: date.strftime("%d/%m/%Y"), "format_date")
