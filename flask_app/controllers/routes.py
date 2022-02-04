from flask_app import app, bcrypt
from flask_app.models import model_members
from flask import redirect, render_template, request, session

@app.route("/")
def login_page():
    if 'user_id' in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = {**request.form}
    is_valid = model_members.Member.validate_member(data)
    if not is_valid:
        return redirect("/")
    hashed_pw = bcrypt.generate_password_hash(data['password'])
    data['password'] = hashed_pw
    member = model_members.Member.save(data)
    session['user_id'] = member
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    is_valid = model_members.Member.validate_login(request.form)
    if not is_valid:
        return redirect("/")
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    del session['user_id']
    return redirect("/")


