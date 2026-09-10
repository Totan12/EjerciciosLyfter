class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un ruido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"


