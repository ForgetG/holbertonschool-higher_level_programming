#!/usr/bin/python3
'''Module for a Singly Linked List'''


class Node:
    '''Class for a Node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''
        Instantiation of the Node

        Args:
            data (int): Data of the Node
            next_node (Node): Next node in the list (optional)
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        Private instance attribute that returns the data of the Node
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        Private instance attribute that sets the data of the Node

        Args: value (int): Given value to set the data of the Node
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''
        Private instance attribute that returns the next node in the list
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        Private instance attribute that sets the next node in the list

        Args: value (Node): Given value to set the next node in the list
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Class for a Singly Linked List'''

    def __init__(self):
        '''Instantiation of the Singly Linked List'''
        self.__head = None

    def __str__(self):
        '''
        Public instance method that returns the list as a string
        '''
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        '''
        Public instance method that inserts a new Node
        into the correct sorted position in the list

        Args: value (int): Given value to insert in the list
        '''
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
