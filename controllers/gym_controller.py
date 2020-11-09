from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository
import repositories.event_repository as event_repository

gyms_blueprint = Blueprint("gyms", __name__)

gyms_blueprint.route("/gyms")
def gyms():
    gyms = gym_repository.select_all() # NEW
    return render_template("gyms/index.html", gyms = gyms)

# # NEW
# # GET '/gyms/new'
@gyms_blueprint.route("/gyms/new", methods=['GET'])
def new_task():
    members = member_repository.select_all()
    events = event_repository.select_all()
    return render_template("gyms/new.html", members = members, events = events)

# # CREATE
# # POST '/gyms'
@gyms_blueprint.route("/gyms",  methods=['POST'])
def create_task():
    member_id = request.form['member_id']
    event_id = request.form['event_id']
    availability = request.form['availability']
    member = member_repository.select(member_id)
    event = event_repository.select(event_id)
    gym = gym(member, event, availability)
    gym_repository.save(gym)
    return redirect('/gyms')


# # DELETE
# # DELETE '/gyms/<id>'
# @gyms_blueprint.route("/gyms/<id>/delete", methods=['POST'])
# def delete_task(id):
#     gym_repository.delete(id)
#     return redirect('/gyms')