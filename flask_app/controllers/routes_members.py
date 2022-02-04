from flask_app import app
from flask_app.models import model_poasts, model_members
from flask import redirect, render_template, request, session

@app.route("/show_profile/<int:id>")
def show_profile(id):
    if 'user_id' not in session:
        return redirect("/")
    member = model_members.Member.get_one({"id": id})
    user = model_members.Member.get_one({'id': session['user_id']})
    return render_template("profile_page.html", member=member, user=user)