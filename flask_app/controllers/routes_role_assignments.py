from flask_app import app
from flask_app.models import model_meetings, model_members, model_role_assignments
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

@app.route("/role_assignment_page")
def role_assignment_page():
    role_assignments = model_role_assignments.RoleAssignment.get_all()
    user = model_members.Member.get_one({'id': session['user_id']})
    return render_template("role_assignment_list.html", role_assignments=role_assignments, user=user)

@app.route("/delete_assignment/<int:id>")
def delete_assignment(id):
    data = {'id': id}
    model_role_assignments.RoleAssignment.delete_one(data)
    return redirect("/role_assignment_page")
