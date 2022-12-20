class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.answer = []
        self.banned = False

    def __add__(self, user):
        kek = User(self.name + user.name)
        kek.points

    def add_points(self, points):
        self.points += points

    def add_answer(self, answer):
        self.answer.append(answer)


class Admin(User):
    def ban(self, user):
        user.banned = True