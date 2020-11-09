import pdb
from models.event import Event
from models.member import Member

import repositories.event_repository as event_repository
import repositories.member_repository as member_repository

event_repository.delete_all()
member_repository.delete_all()

member1 = Member("John", "Male", )
member_repository.save(member1)

member2 = Member("Alex", "Male")
member_repository.save(member2)

member3 = Member("Stacey", "Female")
member_repository.save(member3)

event1 = Event("Salsa", "Dance", "Booked", member1)
event_repository.save(event1)

event2 = Event("Weight Lifting", "Opened", "Exercise", member2)
event_repository.save(event2)

event3 = Event("Badminton", "Sports", "Upcoming", member1)
event_repository.save(event3)



pdb.set_trace()
