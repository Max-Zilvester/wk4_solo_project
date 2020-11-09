class Event:

    def __init__(self, name, category, status, member, id = None):
        self.name = name
        self.category = category
        self.status = status
        self.member = member
        self.id = id