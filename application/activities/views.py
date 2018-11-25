from flask import render_template, redirect, request, url_for

from application import app, db
from .models import Activity
from .forms import ActivityForm

@app.route("/activities", methods=["GET"])
def view_activities():
    return render_template("activities.html", activities=Activity.query.all(), form=ActivityForm())

@app.route("/activities", methods=["POST"])
def add_activity():
    activity = Activity(request.form.get("name"))

    try:
        db.session().add(activity)
        db.session().commit()
    except Exception:
        redirect(url_for("view_activities"))
    
    return redirect(url_for("view_activities"))

@app.route("/activities/delete/<activity_id>/", methods=["POST"])
def delete_activity(activity_id):
    activity = Activity.query.get(activity_id)

    db.session().delete(activity)
    db.session().commit()

    return redirect(url_for("view_activities"))