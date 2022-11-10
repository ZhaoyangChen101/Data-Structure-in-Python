# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Implement the missing functions here below

from linkedlist import LinkedList


class Stack:
    """
    An implementation of a stack structure which utilizes the LinkedList class.

    Attributes:
        stack (LinkedList): A linked list that is used to store the objects added into the stack.
    """
    def __init__(self):
        """Initialize the stack."""
        self.stack = LinkedList()

    def push(self, obj):
        """Add the object 'obj' to the stack."""
        #raise NotImplementedError('Fix me!')
        self.stack.add_last(obj)
        return True

    def pop(self):
        """Return and remove the newest (previously added) object from the stack."""
        #raise NotImplementedError('Fix me!')
        if self.is_empty():
            return None
        else:
            lastPos = self.stack.get_size()-1
            node = self.stack._get_at(lastPos)
            self.stack.remove_position(lastPos)
            return node.obj

    def top(self):
        """Return the newest (previously added) object."""
        #raise NotImplementedError('Fix me!')
        if self.is_empty():
            return None
        else:
            lastPos = self.stack.get_size() - 1
            node = self.stack._get_at(lastPos)
            return node.obj

    def is_empty(self):
        """If stack has no objects, return True, else return False."""
        #raise NotImplementedError('Fix me!')
        return self.stack.get_size() == 0


