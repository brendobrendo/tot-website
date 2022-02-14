from flask_app import app
from flask_app.models import model_role_confirmations
from flask import redirect, request

@app.route("/create_role_confirmation", methods=['POST'])
def confirm_role():
    data = request.form
    model_role_confirmations.RoleConfirmation.confirm_role(data)
    return redirect("/dashboard")

@app.route("/create_volunteer_need", methods=['POST'])
def need_volunteer():
    data = request.form
    model_role_confirmations.RoleConfirmation.need_volunteer(data)
    return redirect("/dashboard")

