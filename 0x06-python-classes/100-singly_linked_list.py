#!/usr/bin/python3
"""Node"""


class Node:
    """Node"""
    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """SEt data"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node"""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """List"""
    __head = None

    def __init__(self):
        pass

    def sorted_insert(self, value):
        """Sort nodes"""
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            previous = None
            current = self.__head
            while current is not None:
                if node.data < current.data:
                    if previous is None:
                        node.next_node = current
                        self.__head = node
                    else:
                        node.next_node = current
                        previous.next_node = node
                    return
                else:
                    previous = current
                    current = current.next_node
            previous.next_node = node

    def __str__(self):
        """Print"""
        out = ""
        current = self.__head
        while current is not None:
            out = out + (str(current.data)) + "\n"
            current = current.next_node
        return out
