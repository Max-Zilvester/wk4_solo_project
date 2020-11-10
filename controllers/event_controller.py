from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.event import Event

import repositories.event_repository as event_repository
import repositories.member_repository as member_repository


events_blueprint = Blueprint("events", __name__)


# INDEX - View all Events (classes) along with event type
@events_blueprint.route("/events")
def events():
    events = event_repository.select_all() # NEW
    return render_template("events/index.html", events=events)
    

# GET new event
@events_blueprint.route("/events/new")
def new_event():
    members = member_repository.select_all()
    return render_template("events/new.html", members=members)

# CREATE new events - posts to server
@events_blueprint.route("/events", methods=['POST'])
def create_event():
    name = request.form['name']
    category = request.form['category']
    status = request.form['status']
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    event = Event(name, category, status, member)
    event_repository.save(event)
    return redirect('/events')

#Show/View
@events_blueprint.route("/events/<id>", methods=['GET'])
def show_event(id):
    event = event_repository.select(id)
    return render_template("events/show.html", event=event)


# EDIT
# GET '/events/<id>/edit'
@events_blueprint.route("/events/<id>/edit", methods=['GET'])
def edit_event(id):
    event = event_repository.select(id)
    members = member_repository.select_all()
    return render_template('events/edit.html', event=event, members=members)

# UPDATE
@events_blueprint.route("/events/<id>", methods=['POST'])
def update_event(id):
    name    = request.form['name']
    category = request.form['category']
    status   = request.form['status']
    member_id = request.form['member_id']
    # member  = member_repository.select()
    
    member = member_repository.select(member_id)
    event = Event(name, category, status, member, id)
    event_repository.update(event)
    return redirect('/events')


# DELETE
@events_blueprint.route("/events/<id>/delete", methods=['POST'])
def delete_event(id):
    event_repository.delete(id)
    return redirect('/events')










# @events_blueprint.route("/events")
# def events():
#     events = event_repository.select_all() # NEW
#     return render_template("events/index.html", events = events)

# @events_blueprint.route("/events/<id>")
# def show(id):
#     event = event_repository.select(id)
#     users = event_repository.users(event)
#     return render_template("events/show.html", event=event, users=users)
