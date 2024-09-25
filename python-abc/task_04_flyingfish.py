#!/usr/bin/python3
'''Module task_04_flyingfish'''


class Fish:
    '''Class Fish'''
    def swim(self):
        '''Action of Fish'''
        print("The fish is swimming")

    def habitat(self):
        '''Habitat of the Fish'''
        print("The fish lives in water")


class Bird:
    '''Class Bird'''
    def fly(self):
        '''Action of the Bird'''
        print("The bird is flying")

    def habitat(self):
        '''Habitat of the Bird'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''Subclass FlyingFish inherits from Fish and Bird'''
    def swim(self):
        '''Action (swim) of the FlyingFish'''
        print("The flying fish is swimming!")

    def fly(self):
        '''Action (fly) of the FlyingFish'''
        print("The flying fish is soaring!")

    def habitat(self):
        '''Habitat of the FlyingFish'''
        print("The flying fish lives both in water and the sky!")
