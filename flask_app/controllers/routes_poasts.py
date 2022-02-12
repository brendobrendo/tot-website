from flask_app import app
from flask_app.models import model_poasts
from flask import redirect, render_template, request, session

@app.route("/create_poast", methods=["POST"])
def create_poast():
    data = {**request.form}
    data['member_id'] = session['user_id']
    model_poasts.Poast.save(data)
    return redirect("/dashboard")

@app.route("/show_poast/<int:id>")
def show_poast(id):
    if 'user_id' not in session:
        return redirect("/")
    poast = model_poasts.Poast.get_one(id)
    if session["user_id"] != poast.member_id:
        return redirect("/daashboard")
    return render_template("/poast_update_form.html")

@app.route("/update_poast/<int:id>", methods=["POST"])
def update_poast(id):
    data = {**request.form}
    data['id'] = id
    model_poasts.Poast.update_one(data)
    return redirect("/dashboard")

@app.route("/delete_poast/<int:id>")
def delete_poast(id):
    model_poasts.Poast.delete_one(id)
    return redirect("/dashboard")
