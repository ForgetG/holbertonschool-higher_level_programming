#!/usr/bin/python3
'''1-my_list module'''


class MyList(list):
    '''Class that inherits from a list'''

    def print_sorted(self):
        '''
        Public instance method that prints the sorted list (ascending order)
        '''
        print(sorted(self))
