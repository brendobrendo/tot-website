from flask_app import app
from flask_app.models import model_meetings, model_members, model_role_names, model_role_assignments, model_poasts, model_officer_titles
from flask import redirect, render_template, request, session
from datetime import datetime

@app.route("/dashboard")
def home_page():
    if 'user_id' not in session:
        return redirect("/")
    user = model_members.Member.get_one({'id': session['user_id']})
    upcoming_roles = model_role_assignments.RoleAssignment.get_upcoming_user({'member_id': session['user_id']})
    next_meeting = model_meetings.Meeting.get_next() # Gives me the id # for the meeting
    next_meeting_date = next_meeting.meeting_date
    next_meeting_roles = model_role_assignments.RoleAssignment.get_upcoming_meeting({"meeting_id": next_meeting.id})
    poasts = model_poasts.Poast.get_all()
    return render_template("home_page.html", user=user, upcoming_roles=upcoming_roles, next_meeting_date=next_meeting_date, next_meeting_roles=next_meeting_roles, poasts=poasts)

@app.route("/create_meeting", methods=["POST"])
def create_meeting():
    model_meetings.Meeting.save(request.form)
    return redirect("/new_meeting")

