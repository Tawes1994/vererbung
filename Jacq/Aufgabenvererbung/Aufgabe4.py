class Lauefer:
    def laufen(self):
        return f"laufen"


class Schwimmer:
    def schwimmen(self):
        return f"Schwimmen"


class Triathleth(Lauefer, Schwimmer):
    pass


player1 = Triathleth()

print(player1.schwimmen())
print(player1.laufen())
