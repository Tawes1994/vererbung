class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt

    def arbeiten(self):
        return f"Mitarbeiter arbeitet!"


class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, teamsize):
        super().__init__(name, gehalt)
        self.teamsize = teamsize

    def arbeiten(self):
        return f"{super().arbeiten()} und leitet das Team"


worker1 = Manager("Bernd", 2000, 5)
worker2 = Mitarbeiter("Christian", 1500)

print(worker1.arbeiten())
