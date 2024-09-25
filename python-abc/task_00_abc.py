from abc import ABC, abstractmethod

class Animal(ABC):
"""so"""
    def sonido(self):
        pass

class Dog(Animal):
    """Dog subclass"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat subclass"""
    def sound(self):
        return "Meow"
