#!/usr/bin/python3
"""7. Singly linked list
    Write a class Node that defines a node of a singly linked list.
"""


class Node:
    """Class Node
        Creation of a node to add a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Init method
            Args:
                data: number to add
                next_node: pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter
            Returns:
                The number to store ina node
        """
        return self.__data

    @data.setter
    def data(self, data):
        """data getter
             Returns:
                instance of data
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """data getter
            Returns:
                The pointer of a next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """data getter
            Returns:
                instance of the next node
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList
        Contain the sorted nodes and str methods
    """
    def __init__(self):
        """Init method
            init head with value None
        """
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert method
            Args:
                value: Node to be inserted
        """
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        elif self.__head.data > value:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None:
                if temp.next_node.data > value:
                    new_node = Node(value, temp.next_node)
                    temp.next_node = new_node
                    return
                temp = temp.next_node
            if temp.next_node is None:
                new_node = Node(value)
                temp.next_node = new_node

    def __str__(self):
        """str method
            build a message with the sorted nodes
        """
        temp = self.__head
        msg = ""
        while temp is not None:
            if temp.next_node is None:
                msg += str(temp.data)
            else:
                msg += str(temp.data) + "\n"
            temp = temp.next_node
        return msg
