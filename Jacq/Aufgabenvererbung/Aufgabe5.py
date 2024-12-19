from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def flaeche(self):
        pass

    def beschreibung(self):
        return "Das ist eine geomethrische Figur"


class Kreis(Figure):
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return 3.14 * self.radius**2


class Rechteck(Figure):
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return self.breite * self.hoehe


kreis = Kreis(5)
rechteck = Rechteck(2, 5)

print(f"Fläche des Kreises: {kreis.flaeche()}")
