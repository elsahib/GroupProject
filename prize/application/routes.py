from application.models import Users, Prizes
# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
# import the app object from the ./application/__init__.py
from application import app, db, bcrypt
# import PostForm from application.forms
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
# import from Flask_login module
from flask_login import login_user, current_user, logout_user, login_required
# import further forms functionality
import requests

# define routes for / & /home, this function will be called when these are accessed
# General site information accessable to everyone
#========== Home Page ========================
@app.route('/')
@app.route('/home')
def home():


    return render_template('home.html', title='Home')

#========== Generate Page ====================
@app.route('/gen')
@login_required
def gen():
    response = requests.get('http://przgen:8000/home')
    code = str(response.json()["code"])
    prize = str(response.json()["prize"])
    prizeData = Prizes(code =code, prize = prize, id = current_user.id)
    db.session.add(prizeData)
    db.session.commit()
    return render_template('home.html', title='Home', code=code, prize=prize)


#========= View prizes =======================
@app.route('/view/<int:num>')
@login_required
def view(num):
    per_page = 10
    prizes = db.session.query(Prizes).select_from(Prizes).filter_by(id = current_user.id).paginate(per_page = per_page, page = num, error_out=True )
    
    return render_template('prize2.html', title='View prizes', prizes=prizes)

#========= remove prizes =====================
@app.route('/deleteprize/<prize_id>')
@login_required
def deleteprize(prize_id):

    db.session.query(Prizes).filter_by(prize_id = prize_id).delete(synchronize_session=False)
    db.session.commit()
    return redirect(url_for('view', num=1))



########### User Management ##################
#========== User Registration Page ===========
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#========== User Login  ======================
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

#========= User Logout =======================
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#========= Manage User Account ===============
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('account.html', title='Account', form=form)

#========= Delete User Account ================
@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    prizes = prizes.query.filter_by(id=user)
    for prize in prizes :
        db.session.delete(prize)
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))