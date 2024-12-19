class Fahrzeug:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def beschreiben(self):
        return f"Das Fahrzeug ist von der Marke {self.marke} und hat die Farbe {self.farbe}."


class Auto(Fahrzeug):
    def __init__(self, marke, farbe, anzahl_tueren):
        super().__init__(marke, farbe)
        self.anzahl_tueren = anzahl_tueren

    def beschreiben(self):
        return f"Das Auto ist von der Marke {self.marke}, hat die Farbe {self.farbe} und {self.anzahl_tueren} Türen."


fahrzeug1 = Fahrzeug("BMW", "Rot")
print(fahrzeug1.beschreiben())

auto1 = Auto("Mercedes", "Schwarz", 4)
print(auto1.beschreiben())
