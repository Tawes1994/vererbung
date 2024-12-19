""" class Person:
    def __init__(self, name):
        self.name = name
 
person = Person("Maggie Simpson")
print(person.name) """

# Zugriff protected
""" class Person:
    def __init__(self, name):
        self._name = name
 
 
person = Person("Marge Simpson")
print(person._name) # möglich aber nicht empfohlen
person._name = "Olaf"
print(person._name) # möglich aber nicht empfohlen
 
class Student(Person):
 
    def get_name(self):
        return self._name
   
 
student = Student("Homer Simpson")
print(student.get_name()) """


# Zugriff private


class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):  # Getter Methode
        return person.__name

    def set_name(self, new_name):  # Setter Methode zum setzen neuer Werte
        self.__name = new_name


person = Person("Lisa Simpson")
print(person.get_name())  # Ruft die Methode get_name auf um Namen zu lesen

person.set_name("Pascal")  # Setzt den Wert des Attributs auf einen neuen Wert
print(person.get_name())

# Aufgabe 1


class Auto:

    def __init__(self, marke):
        self.marke = marke


mein_auto = Auto("Audi")

print(mein_auto.marke)

# Aufgabe 2


class Buch:
    def __init__(self, title):
        self._title = title

    def get_title(self):  # Getter Methode
        return self._title


Mein_Buch = Buch("Harri Knitter")
print(Mein_Buch.get_title())  # Ruft die Methode get_name auf um Namen zu lesen

# Aufgabe 3


class Person:
    def __init__(self, name) -> None:
        self._name = name


class Student(Person):
    def get_name(self) -> str:
        return self._name


name = Student("Dieter")

print(name._name)
