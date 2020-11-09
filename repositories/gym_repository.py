from db.run_sql import run_sql

from models.gym import Gym
from models.member import Member
from models.event import Event
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository
import repositories.event_repository as event_repository

# Populating the database.
def save(gym):
    sql = "INSERT INTO gyms ( member_id, event_id, availability ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [gym.member.id, gym.event.id, gym.availability]
    results = run_sql( sql, values )
    gym.id = results[0]['id']
    return gym

def select_all():
    gyms = []

    sql = "SELECT * FROM gyms"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        event = event_repository.select(row['event_id'])
        gym = Gym(member, event, row['availability'], row['id'])
        gyms.append(gym)
    return gyms

def delete_all():
    sql = "DELETE FROM gyms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)