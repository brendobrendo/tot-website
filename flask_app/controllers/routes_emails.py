from flask_app import app
from flask_app.models import model_members
from flask import redirect, render_template, request, session
import smtplib

@app.route("/new_email")
def new_email():
    if 'user_id' not in session:
        return redirect("/")
    user = model_members.Member.get_one({'id': session['user_id']})
    return render_template("toastmaster_email.html", user=user)

@app.route("/send_email", methods=['POST'])
def send_email():
    data = request.form
    title = data.get("title")
    content = data.get("content")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("tot4741.toastmaster@gmail.com", "toastmaster4741")

    server.sendmail("tot4741.toastmaster@gmail.com", "brendan.smith903@gmail.com", content)
    return redirect("/officers_page")