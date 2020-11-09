from db.run_sql import run_sql
from models.member import Member
from models.event import Event

def save(member):
    sql = "INSERT INTO members( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['id'] )
    return member


def events(member):
    events = []

    sql = "SELECT events.* FROM events INNER JOIN gyms ON gyms.event_id = events.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        event = event(row['name'], row['type'], row['id'])
        events.append(event)

    return events


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)