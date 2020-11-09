from db.run_sql import run_sql
from models.member import Member
from models.event import Event
import repositories.member_repository as member_repository

def save(event):
    sql = "INSERT INTO events(name, category, status, member_id) VALUES ( %s, %s, %s, %s ) RETURNING *"
    values = [event.name, event.category, event.status, event.member.id]
    results = run_sql( sql, values )
    event.id = results[0]['id']
    return event


def select_all():
    events = []

    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        event = Event(row['name'], row['category'], row['status'], member, row['id'])
        events.append(event)
    return events


def select(id):
    event = None
    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repository.select(result['member_id'])
        event = Event(result['name'], result['category'], result['status'], member, result['id'] )
    return event


def members(event):
    members = []

    sql = "SELECT * FROM members WHERE event_id = %s"
    values = [event.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['gender'], row['id'])
        members.append(member)

    return members


def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)

def update(event):
    sql = "UPDATE events SET (title, genre, publisher, author_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [event.title, event.genre, event.publisher, event.author.id, event.id]
    print(values)
    run_sql(sql, values)