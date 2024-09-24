#!/usr/bin/python3
'''Module task_00_abc'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''Abstract class Animal using ABC package'''
    @abstractmethod
    def sound(self):
        '''Abstract method sound'''
        pass


class Dog(Animal):
    '''Abstract subclass Dog inherits from Animal'''
    def sound(self):
        '''Abstract method sound'''
        return "Bark"


class Cat(Animal):
    '''Abstract subclass Cat inherits from Animal'''
    def sound(self):
        '''Abstract method sound'''
        return "Meow"
