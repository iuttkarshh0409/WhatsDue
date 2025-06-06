# whatsdue-frontend/routes.py

from flask import Blueprint, render_template

frontend_routes = Blueprint('frontend', __name__)

@frontend_routes.route('/')
def home():
    return render_template('index.html')
