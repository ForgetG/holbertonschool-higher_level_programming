#!/usr/bin/python3
'''Module task_05_dragon'''


class SwimMixin:
    '''Mixin class SwimMixin'''
    def swim(self):
        '''Method to print action of swimming'''
        print("The creature swims!")


class FlyMixin:
    '''Mixin class FlyMixin'''
    def fly(self):
        '''Method to print action of flying'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''Class Dragon inherits from SwimMixin and FlyMixin'''
    def roar(self):
        '''Method to print the action of roaring'''
        print("The dragon roars!")
