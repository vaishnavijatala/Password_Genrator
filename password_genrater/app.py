from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, SavedPassword
from password_utils import generate_password
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash("Username already exists.")
            return redirect(url_for('signup'))

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created! Please login.")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials.")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    passwords = SavedPassword.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', passwords=passwords)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        length = int(request.form['length'])

        # Checkboxes
        use_lower = 'lowercase' in request.form
        use_upper = 'uppercase' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form
        exclude_similar = 'exclude_similar' in request.form
        exclude_ambiguous = 'exclude_ambiguous' in request.form

        pwd, strength = generate_password(length, use_lower, use_upper, use_digits, use_symbols, exclude_similar, exclude_ambiguous)

        new_entry = SavedPassword(
            title=title,
            password=pwd,
            user_id=session['user_id']
        )
        db.session.add(new_entry)
        db.session.commit()

        flash("Password generated and saved!")
        return redirect(url_for('dashboard'))

    return render_template('generate.html')

if __name__ == '__main__':
    app.run(debug=True)
