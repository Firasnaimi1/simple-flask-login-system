from flask import Blueprint, render_template, request, redirect , url_for ,flash
from flask_login import login_user
from werkzeug.security import generate_password_hash
from database import Session
from models import User

register_bp = Blueprint("register" , __name__)


@register_bp.route('/register' , methods=["GET" , "POST"])

def register():

    if request.method == "POST":
        with Session() as session_db :
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            passwordc = request.form['passwordc']

            existing_email = session_db.query(User).filter_by(email=email).first()

            if existing_email:
                flash("this email is already registered", "danger")
                return redirect(url_for('register.register'))
            elif password != passwordc:
                flash("Passwords do not match", "danger")
                return redirect(url_for('register.register'))

            else :
                new_user = User(name=name, email=email , password = generate_password_hash(password) )
                session_db.add(new_user)
                try :
                    session_db.commit()
                    login_user(new_user)
                    flash('you successfully created an account' , "success")
                    return redirect(url_for('login.login'))
                except Exception as e:
                    session_db.rollback()
                    flash("an error occured, Please try again later" , "danger")
                    return redirect(url_for('register.register'))
    
    return render_template('register.html')

