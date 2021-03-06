"""
Main Flask driver. Creates and launches our instance of
a Flask app.
"""

from flask import Flask
from views import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
