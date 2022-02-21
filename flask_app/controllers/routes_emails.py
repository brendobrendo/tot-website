from flask_app import app
from flask_app.models import model_members, model_officers, model_role_assignments
from flask import redirect, render_template, request, session
import smtplib
from email.message import EmailMessage


@app.route("/new_email")
def new_email():
    if 'user_id' not in session:
        return redirect("/")
    user = model_members.Member.get_one({'id': session['user_id']})
    return render_template("toastmaster_email.html", user=user)


@app.route("/send_email", methods=['POST'])
def send_email():
    data = request.form
    subject = data.get("subject")
    body = data.get("body")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "tot4741.toastmaster@gmail.com"
    msg['To'] = "brendan.smith903@gmail.com"
    msg.set_content(body)

    upcoming_roles = model_role_assignments.RoleAssignment.get_upcoming_user(
        {'member_id': session['user_id']})
    upcoming_role = upcoming_roles[0].role_name

    msg.add_alternative("""
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:blue;">
    """ +
                        f'{body} </h1>' +
            "<p>Upcoming Role: " + f'{upcoming_role} </p>' +
                        """
        </body>
    </html>
    """, subtype='html')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("tot4741.toastmaster@gmail.com", "toastmaster4741")

    """
    officers = model_officers.Officer.get_all()
    for officer in officers:
        server.sendmail("tot4741.toastmaster@gmail.com", officer.email, content)
    """

    server.send_message(msg)

    server.quit()
    return redirect("/officers_page")
