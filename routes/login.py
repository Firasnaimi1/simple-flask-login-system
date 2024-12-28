from flask import Blueprint, render_template, request, redirect , url_for ,flash
from flask_login import login_user
from werkzeug.security import check_password_hash
from database import Session
from models import User


login_bp = Blueprint("login" , __name__)

@login_bp.route('/login' , methods = ["GET" , "POST"])
def login():
    if request.method == "POST":
        with Session() as session_db :
            email = request.form['email']
            password = request.form['password']

            user = session_db.query(User).filter_by(email=email).first()

            if user and check_password_hash(user.password , password):
                login_user(user)
                flash('you successfully logged in' , "info")
                return redirect(url_for('dashboard.dashboard'))
            else : 
                flash('Invalid email or password' , "danger")
    
    return render_template('login.html')


