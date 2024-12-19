class Bankkonto:
    def __init__(self, kontonummer, kontostand):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand += betrag
        print(f"{betrag} wurde eingezahlt. Neuer Kontostand: {self.kontostand} €")

    def auszahlen(self, betrag):
        if betrag > self.kontostand:
            print(f"nicht genug Geld auf dem Konto")
        else:
            self.kontostand -= betrag
        print(f"{betrag} wurde abgehoben. Neuer Kontostand: {self.kontostand} €")


class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, kontostand, zins_satz):
        super().__init__(kontonummer, kontostand)
        self.zins_satz = zins_satz

    def zinsen(self):
        if self.kontostand > 0:
            zinsen = self.kontostand * (self.zins_satz / 100)
            print(
                f"Die Zinsen in diesem Jahr betragen bei aktuellem Kontostand {zinsen} €"
            )
            return zinsen
        else:
            print("Kein Guthaben für Zinsen vorhanden!")


class Girokonto(Bankkonto):
    def __init__(self, kontonummer, kontostand, dispo):
        super().__init__(kontonummer, kontostand)
        self.dispo = dispo

    def auszahlen(self, betrag):
        if self.kontostand - betrag < self.dispo:
            print(f"Keine Auszahlung möglich dispo überschritten {self.dispo} €")
        else:
            self.kontostand -= betrag
            print(f"{betrag} wurde ausgezahlt. Neuer Kontostand {self.kontostand} €")


konto1 = Bankkonto("12345", 1000)
konto2 = Sparkonto("54321", 2000, 2.5)
konto3 = Girokonto("67890", 2000, -1000)

konto1.einzahlen(500)
konto1.auszahlen(800)

konto3.einzahlen(11200)
konto3.auszahlen(100)
konto3.auszahlen(500)
