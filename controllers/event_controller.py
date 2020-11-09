from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.event import Event
import repositories.event_repository as event_repository

events_blueprint = Blueprint("events", __name__)


# INDEX - View all Events (classes) along with event type
@events_blueprint.route("/events")
def events():
    events = event_repository.select_all() # NEW
    return render_template("events/index.html", events = events)

#Show/View
@events_blueprint.route("/events/<id>")
def show(id):
    event = event_repository.select(id)
    return render_template("events/show.html", event=event)

# NEW

# CREATE

# EDIT

# UPDATE

# DELETE











# @events_blueprint.route("/events")
# def events():
#     events = event_repository.select_all() # NEW
#     return render_template("events/index.html", events = events)

# @events_blueprint.route("/events/<id>")
# def show(id):
#     event = event_repository.select(id)
#     users = event_repository.users(event)
#     return render_template("events/show.html", event=event, users=users)
