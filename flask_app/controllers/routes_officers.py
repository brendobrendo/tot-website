from flask_app import app
from flask_app.models import model_officers, model_role_names, model_members, model_meetings
from flask import redirect, render_template, request, session

@app.route("/officers_page")
def officers_page():
    if 'user_id' not in session:
        return redirect("/")
    user = model_members.Member.get_one({'id': session['user_id']})
    if not user.officer_key:
        return redirect("/dashboard")
    locations = [{'name': 'Zoom', 'value': 1}, {'name': 'In-person', 'value': 2}]
    meeting_roles = model_role_names.RoleName.get_all()
    members = model_members.Member.get_all()
    meetings = model_meetings.Meeting.get_all()
    return render_template("officers_page.html", user=user, locations=locations, meeting_roles=meeting_roles, members=members, meetings=meetings) 


@app.route("/create_officer_assignments", methods=["POST"])
def create_officer_assignments():
    if 'user_id' not in session:
        return redirect("/")
    data = {**request.form}
    officer_ids = list(data)
    member_ids = list((data.values()))

    officer_entries = []
    for index_value in range(0, len(officer_ids)):
        entry = {}
        entry['officer_role_name_id'] = officer_ids[index_value]
        entry['member_id'] = member_ids[index_value]
        officer_entries.append(entry)
    
    for entry in officer_entries:
        model_officers.Officer.save(entry)

    return redirect("/new_meeting")