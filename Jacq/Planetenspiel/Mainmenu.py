from Planeten import Planet
from Human import Human
import os
import time


class hauptmenu:
    def __init__(self):
        self.running = True
        self.planets = []

    def Mainmenu_choice(self):
        while self.running:
            self.planeten_ausgeben()
            try:
                choice = int(
                    input(
                        """
            Wie kann man dir helfen?
            1: Neuen Planeten erstellen
            2: Menschen erschaffen
            3: Gebäude erstellen
            4: Programm beenden
            """
                    )
                )
            except:
                print("Das war keine Zahl!")

            if choice == 1:
                self.neuer_planet()
            elif choice == 2:
                self.menschen_erschaffen()
            elif choice == 3:
                self.gebaeude_erstellen()
            elif choice == 4:
                self.beenden()

    def neuer_planet(self):
        name = input("Gib bitte einen Namen ein: ")
        planet = Planet(name)
        self.planets.append(planet)
        print(f"Der Planet: {planet.name} wurde erfolgreich erstellt.")
        time.sleep(1)
        os.system("cls")

    def menschen_erschaffen(self):
        selected_planet = self.planeten_auswahl()

        name = input("Gib den Namen des Menschen ein: ")
        alter = int(input("Gib das Alter des Menschen ein: "))
        beruf = input("Gib den Beruf des Menschen ein: ")
        new_human = Human(name, alter, beruf)

        selected_planet.add_human(new_human)

    def gebaeude_erstellen(self):
        buildings = [
            {
                "name": "Rathaus",
                "food_costs": 50,
                "stone_costs": 1200,
                "wood_costs": 1200,
                "gold_costs": 80,
            },
            {
                "name": "Jagdhütte",
                "food_costs": 10,
                "stone_costs": 10,
                "wood_costs": 200,
                "gold_costs": 30,
            },
            {
                "name": "Bauernhof",
                "food_costs": 20,
                "stone_costs": 400,
                "wood_costs": 1200,
                "gold_costs": 50,
            },
            {
                "name": "Holzfällerhütte",
                "food_costs": 10,
                "stone_costs": 100,
                "wood_costs": 300,
                "gold_costs": 25,
            },
            {
                "name": "Steinbruch",
                "food_costs": 15,
                "stone_costs": 100,
                "wood_costs": 1200,
                "gold_costs": 25,
            },
            {
                "name": "Goldmine",
                "food_costs": 40,
                "stone_costs": 1500,
                "wood_costs": 1500,
                "gold_costs": 30,
            },
        ]

        selected_planet = self.planeten_auswahl()

        print("\nWähle ein Gebäude aus:")
        for i, building in enumerate(buildings):
            print(
                f"{i + 1}: {building['name']} (Nahrung: {building['food_costs']}, Stein: {building['stone_costs']}, Holz: {building['wood_costs']}, Gold: {building['gold_costs']})"
            )

        try:
            building_choice = int(input("Gebäude-Nummer: ")) - 1
            if not (0 <= building_choice < len(buildings)):
                raise IndexError("Ungültiger Gebäude-Index")
            selected_building = buildings[building_choice]
        except (IndexError, ValueError):
            print("Ungültige Auswahl!")
            time.sleep(1)
            return

        if building_choice != 0:
            print("Sie müssen zuerst ein Rathaus bauen!")
            return

        if (
            selected_building["name"] == "Rathaus"
            and "Rathaus" not in selected_planet.buildings
        ):
            Planet.build_rathaus(selected_planet)
            return
        elif (
            selected_building["name"] == "Rathaus"
            and "Rathaus" not in selected_planet.buildings
        ):
            print(f"Das Gebäude {selected_building['name']} wurde erfolgreich gebaut!")
            selected_planet.buildings.append(selected_building["name"])
        else:
            print(
                f"Hier gibt es bereits ein Rathaus oder das Gebäude kann nicht gebaut werden."
            )

    def planeten_auswahl(self):
        if not self.planets:
            print("Es gibt keine Planeten, auf denen ein Gebäude erstellt werden kann.")
            time.sleep(0.5)
            return

        print("Wähle einen Planeten aus:")
        for i, planet in enumerate(self.planets):
            print(f"{i + 1}: {planet}")

        try:
            planet_choice = int(input("Planeten-Nummer: ")) - 1
            if not (0 <= planet_choice < len(self.planets)):
                raise IndexError("Ungültiger Planeten.")
            selected_planet = self.planets[planet_choice]
            return selected_planet
        except (IndexError, ValueError):
            print("Ungültige Auswahl.")
            time.sleep(1)
            return

    def planeten_ausgeben(self):
        if not self.planets:
            print("Es gibt keine Planeten.")
        else:
            for i in self.planets:
                print(i)

    def beenden(self):
        exit()


if __name__ == "__main__":
    menu = hauptmenu()
    menu.Mainmenu_choice()
