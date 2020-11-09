import pdb
from models.event import Event
from models.member import Member
from models.gym import Gym

import repositories.event_repository as event_repository
import repositories.member_repository as member_repository
import repositories.gym_repository as gym_repository 

gym_repository.delete_all()
event_repository.delete_all()
member_repository.delete_all()

member1 = Member('John')
member_repository.save(member1)

member2 = Member('Alex')
member_repository.save(member2)

member3 = Member('Stacey')
member_repository.save(member3)

event1 = Event('Salsa', 'Dance')
event_repository.save(event1)

event2 = Event('Weight Lifting', 'Exercise')
event_repository.save(event2)

event3 = Event('Badminton', 'Sports')
event_repository.save(event3)

gym1 = Gym(member1, event1, 'Yes')
gym_repository.save(gym1)

gym2 = Gym(member2, event2, 'No')
gym_repository.save(gym2)

gym3 = Gym(member3, event3, 'Upcoming')
gym_repository.save(gym3)

pdb.set_trace()
