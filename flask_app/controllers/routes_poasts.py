from flask_app import app
from flask_app.models import model_poasts
from flask import redirect, render_template, request, session

@app.route("/create_poast", methods=["POST"])
def create_poast():
    data = {**request.form}
    data['member_id'] = session['user_id']
    model_poasts.Poast.save(data)
    return redirect("/dashboard")