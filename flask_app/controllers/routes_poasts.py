from flask_app import app
from flask_app.models import model_poasts, model_members
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
    user = model_members.Member.get_one({'id': session['user_id']})
    poast = model_poasts.Poast.get_one({'id': id})
    if session["user_id"] != poast.member_id:
        return redirect("/dashboard")
    return render_template("/show_poast.html", user=user, poast=poast)

@app.route("/update_poast", methods=["POST"])
def update_poast():
    data = request.form
    model_poasts.Poast.update_one(data)
    return redirect("/dashboard")

@app.route("/delete_poast/<int:id>")
def delete_poast(id):
    model_poasts.Poast.delete_one(id)
    return redirect("/dashboard")
