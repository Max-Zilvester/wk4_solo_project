from db.run_sql import run_sql
from models.member import Member
from models.event import Event

def save(member):
    sql = "INSERT INTO members(name, gender) VALUES ( %s, %s) RETURNING *"
    values = [member.name, member.gender]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['gender'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['gender'], result['id'] )
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (name, gender) = (%s, %s) WHERE id = %s"
    values = [member.ame, member.gender, member.id]
    run_sql(sql, values)


def events(member):
    events = []

    sql = "SELECT * FROM events WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        event = event(row['name'], row['category'], row['status'], row['member_id'], row['id'])
        events.append(event)

    return events


