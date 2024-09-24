#!/usr/bin/python3
'''Module task_02_verboselist'''


class VerboseList(list):
    '''Class VerboseList inherits list'''

    def append(self, item):
        '''Public instance method append'''
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        '''Public instance method extend'''
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        '''Public instance method remove'''
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
