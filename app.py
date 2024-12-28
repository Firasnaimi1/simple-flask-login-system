from flask import Flask, redirect , url_for
from flask_login import LoginManager, current_user
from database import create_tables
from routes.register import register_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.dashboard import dashboard_bp
from datetime import timedelta

app = Flask(__name__)


app.secret_key = 'your_secret_key_here' #use complex secret key
app.permanent_session_lifetime = timedelta(minutes=5)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login' 
login_manager.login_message = "please login first, or create an account if you don't have one."
login_manager.login_message_category = "danger"

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    return redirect(url_for('login.login'))

create_tables()

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(dashboard_bp)


@login_manager.user_loader
def load_user(user_id):
    from models import User  
    from database import Session
    with Session() as session_db:
        return session_db.query(User).get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True) 
