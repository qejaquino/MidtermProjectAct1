from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/index', methods=['GET', 'POST'])
def home1():
    return render_template("home.html", user=current_user)

@views.route('/account')
@login_required
def account():
    all_data = User.query.all()
    return render_template("account.html", user=current_user, users=all_data)

@views.route('/about')
def about():
    return render_template("about.html", user=current_user)
