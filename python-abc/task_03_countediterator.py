#!/usr/bin/python3
'''Module task_03_countediterator.py'''


class CountedIterator:
    '''Class CountedIterator'''
    def __init__(self, iterable):
        '''Instantiation of CountedIterator class'''
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        '''
        Public instance method get_count:
            get the current count of items iterated over
        '''
        return self.count

    def __next__(self):
        '''Get the next item from the iterator and increment count'''
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        '''Return the iterator object'''
        return self
