import random


class Human:
    def __init__(self, name, alter, beruf):
        self.name = name
        self.alter = alter
        self.beruf = beruf

    def details(self):
        return f"Name: {self.name}, Alter: {self.alter}, Beruf: {self.beruf}"
