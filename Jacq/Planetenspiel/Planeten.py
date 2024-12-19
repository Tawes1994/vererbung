import random


class Planet:

    def __init__(self, name):
        self.name = name
        self.population = 0
        self.einwohner = []
        self.food = random.randint(300, 2000)
        self.holz = random.randint(1500, 2000)
        self.stein = random.randint(1500, 2000)
        self.gold = 200
        self.buildings = []
        self.rathaus_built = False

    def details(self):
        return f"Name: {self.name}, Population: {self.population}, Nahrung: {self.food} Gold: {self.gold}, Holz: {self.holz}, Stein: {self.stein}"

    def add_human(self, human):
        if "Rathaus" not in self.buildings:
            print("Baue zuerst ein Rathaus.")
        else:
            if self.population < 20:
                self.einwohner.append(human)
                self.population += 1
                print(f"{human.name} wurde dem Planeten {self.name} hinzugefügt.")
            else:
                print(f"Die maximale Bevölkerungszahl auf {self.name} wurde erreicht.")

    def has_enough_resources_for_rathaus(self):
        rathaus_costs = {"food": 50, "stone": 1200, "wood": 1200, "gold": 80}
        return (
            self.food >= rathaus_costs["food"]
            and self.stein >= rathaus_costs["stone"]
            and self.holz >= rathaus_costs["wood"]
            and self.gold >= rathaus_costs["gold"]
        )

    def build_rathaus(self):

        if self.has_enough_resources_for_rathaus():
            self.food -= 50
            self.stein -= 1200
            self.holz -= 1200
            self.gold -= 80
            self.buildings.append("Rathaus")
            self.rathaus_built = True
            print(f"Das Rathaus wurde auf {self.name} gebaut!")
        else:
            print(f"Nicht genug Ressourcen, um ein Rathaus auf {self.name} zu bauen.")

    def __str__(self):
        return (
            f"Planet: {self.name}, "
            f"Bevölkerung: {self.population}/20, Nahrung: {self.food} "
            f"Rohstoffe: Holz={self.holz}, Stein={self.stein}, Gold={self.gold}"
        )
