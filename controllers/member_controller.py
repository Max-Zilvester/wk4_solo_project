from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.event_repository as event_repository

members_blueprint = Blueprint("members", __name__)


# INDEX - View all Members (classes) along with member type
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all() # NEW
    return render_template("members/index.html", members=members)


@members_blueprint.route("/members/new",  methods=['GET'])
def display_show_member():
    return render_template("members/new.html")

    
#     return render_template("members/new.html")

@members_blueprint.route("/members",  methods=['POST'])
def create_member():
    name = request.form["name"]
    gender = request.form["gender"]
    member = Member(name, gender)
    member_repository.save(member)
    return redirect("/members")

# EDIT
# GET '/members/<id>/edit'
@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    event = event_repository.select_all()
    return render_template('members/edit.html', event=event, member=members)
    

# UPDATE
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name    = request.form['name']
    gender = request.form['gender']
    event_id = request.form['event_id']
    # member  = member_repository.select()
    
    event = event_repository.select(event_id)
    member = Member(name, gender, id)
    member_repository.update(member)
    return redirect('/members')

    # event = request.form['event'] USE $ EVENTS
    # type = request.form['type']


# def create_task():
#     member_id = request.form['member_id']
#     event_id = request.form['event_id']
#     availability = request.form['availability']
#     member = member_repository.select(member_id)
#     event = event_repository.select(event_id)
#     gym = gym(member, event, availability)
#     gym_repository.save(gym)
#     return redirect('/gyms')

# @members_blueprint.route("/members/<id>")
# def show(id):
#     #user = user_repository.select(id)
#     member = member_repository.events(member)
#     return render_template("members/show.html", member=member)


# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = user_repository.location(user)
#     return render_template("user/show.html", users=users, location=location)


    # location = location_repository.select(id)
    # users = location_repository.users(location)
    # return render_template("locations/show.html", location=location, users=users)