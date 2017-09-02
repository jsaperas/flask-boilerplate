"""
Views.py contains all the flask routes
"""
from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__,
                      template_folder='templates')

@blueprint.route('/')
def index():
    """
    Returns index.html page.
    """
    return render_template('index.html')
