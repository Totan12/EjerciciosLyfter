"""
Módulos de funcionalidades independientes (Mixins): Permite crear clases pequeñas y muy 
específicas (como tus clases de poderes: Fly, Teleportation) que no están pensadas para 
usarse solas, sino para ser "acopladas" a otras clases más grandes para darles superpoderes 
o herramientas extra.


Separación de responsabilidades: Ayuda a que tu código no esté en un solo bloque gigante. 
Puedes tener la lógica de la base de datos por un lado, la lógica de la interfaz gráfica
por otro, y unificar ambas en un componente final mediante herencia.


Modelado del mundo real: Facilita la representación de objetos complejos que pertenecen 
legítimamente a dos categorías distintas a la vez (por ejemplo, un RelojInteligente que
hereda tanto de Reloj como de DispositivoElectronico).

---Esta informacion es un resumen realizado por gemini---
     ---para lo investigado de la herencia multiple---
"""

class Fly:
    def fly(self):
        print("Puedes volar")

class Teleportation:
    def teleportation(self):
        print("Puedes teletrasportarte")

class Regeneration:
    def regeneration(self):
        print("Te puedes regenerar")

class SuperHero(Fly, Teleportation, Regeneration):
    def __init__(self, name, alias, age):
        self.name = name
        self.alias = alias
        self.age = age

    def introduce(self):
        print(f"Hola mi nombre es {self.name}, mi alias es {self.alias} y tengo {self.age} años.")

