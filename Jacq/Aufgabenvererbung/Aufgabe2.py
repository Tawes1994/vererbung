class Tier:
    def __init__(self, name, art):
        self.name = name
        self.art = art

    def gib_laut(self):
        return f"Geräusch"

    def info(self):
        return f"Das Tier heißt {self.name}"


class Hund(Tier):
    def gib_laut(self):
        return f"Quietsch"

    def info(self):
        return f"{super().info()} und es ist ein {self.art}"


class Katze(Tier):
    def gib_laut(self):
        return f"Miau"

    def info(self):
        return f"{super().info()} und es ist ein {self.art}"


class Maus(Tier):
    def gib_laut(self):
        return f"Pieps"

    def info(self):
        return f"{super().info()} und es ist ein {self.art}"


class Chinchilla(Tier):
    pass

    def info(self):
        return f"{super().info()} und es ist ein {self.art}"


tier1 = Chinchilla("Bernd", "Chinchilla")
tier2 = Hund("Dieter", "Hund")

print(tier2.info())

print(tier1.info())
