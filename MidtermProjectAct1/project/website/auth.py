from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.json import jsonify
import sqlite3  
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Incorrect username / password try again.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/insert',methods=['GET','POST'])
@login_required
def insert():
    if request.method == 'POST':
        data = request.get_json()
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        password = data.get('password')
        birthdate = data.get('birthDate')
        phone = data.get('Phone')
        course = data.get('course')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            #insert account.
            insert_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'), birth_date=birthdate, phone=phone, course=course)
            db.session.add(insert_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.account'))
    
    return render_template("account.html", user=current_user)


@auth.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        data = request.get_json()
        user.first_name = data.get('firstName')
        user.last_name = data.get('lastName')
        user.birth_date = data.get('birthDate')
        user.course = data.get('course')
        user.email = data.get('email')
        user.phone = data.get('phone')
        try:
            db.session.commit()
            flash("Account Updated Successfully")
            return redirect(url_for('views.account'))
        except:
            return "There's was a problem updating accounts."
    else:
        return render_template("account.html", user=current_user)

@auth.route('/delete/<int:id>',methods = ['GET', 'POST'])
def delete(id):
    account = User.query.get(id)
    db.session.delete(account)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('views.account'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        password1 = data.get('password1')
        password2 = data.get('password2')
        birthdate = data.get('birthDate')
        phone = data.get('Phone')
        course = data.get('course')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #User account Creation
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'), birth_date=birthdate, phone=phone, course=course)
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


# @auth.route('/test')
# def account():
#     all_data = User.query.all()

#     for user in all_data:
#         print(user.first_name)
#         return jsonify(f"<id={user.first_name}, username={user.last_name}>")


@auth.route('/Mlogin', methods=['POST'])
def login1():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print('Logged in successfully!')
                return "", 200
            else:
                print('Invalid Login!')
                return "", 403
        else:
            print('Invalid Login!')
            return "", 403