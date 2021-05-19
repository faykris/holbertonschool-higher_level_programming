"""7 - Singly linked list
    Write a class Node that defines a node of a singly linked
"""


class Node:
    """Node
        Class when i can work with a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Init method
        Args:
            data:
            next_node:
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ data getter:
            Take the information
        """
        pass

    @data.setter
    def data(self, value):
        """ data setter:
            Validate the information
        """
        pass

    @property
    def next_node(self):
        """ data getter:
            Take the information
        """
        pass

    @next_node.setter
    def next_node(self, value):
        """ next_node setter:
            Validate the information
        """
        pass


class SinglyLinkedList:
    """SinglyLinkedList
        class that define a singly linked list
    """

    def __init__(self):
        """Init method
            No arguments yet
        """
        pass

    def sorted_insert(self, value):
        pass
