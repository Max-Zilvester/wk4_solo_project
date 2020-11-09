from db.run_sql import run_sql
from models.member import Member
from models.event import Event

def save(event):
    sql = "INSERT INTO events(name, type) VALUES ( %s, %s ) RETURNING id"
    values = [event.name, event.type]
    results = run_sql( sql, values )
    event.id = results[0]['id']
    return event


def select_all():
    events = []

    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        event = Event(row['name'], row['type'], row['id'])
        events.append(event)
    return events


def select(id):
    event = None
    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        event = Event(result['name'], result['type'], result['id'] )
    return event


def members(event):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN gyms ON gyms.member_id = members.id WHERE event_id = %s"
    values = [event.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)

    return members


def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)