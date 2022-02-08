from flask_app import app
from flask_app.models import model_meetings, model_members, model_role_names, model_role_assignments
from flask import redirect, render_template, request, session

@app.route("/create_meeting_assignments", methods=["POST"])
def create_meeting_assignments():
    if 'user_id' not in session:
        return redirect("/")
    data = {**request.form}
    role_ids = list(data)
    member_ids = list((data.values()))
    meeting_id = member_ids[0]

    role_entries = []
    for index_value in range(1, len(role_ids)):
        entry = {}
        entry['role_name_id'] = role_ids[index_value]
        entry['member_id'] = member_ids[index_value]
        entry['meeting_id'] = meeting_id
        role_entries.append(entry)
    
    for entry in role_entries:
        model_role_assignments.RoleAssignment.save(entry)

    return redirect("/officers_page")