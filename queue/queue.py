# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Implement the missing functions here below

from linkedlist import LinkedList

class Queue:

    #​‌​​​​​‌‌‌​‌​​​ An implementation of a queue structure which utilizes the LinkedList class.

    #​‌​​​​​‌‌‌​‌​​​ Attributes:
    #​‌​​​​​‌‌‌​‌​​​ queue (LinkedList): A linked list that is used to store the objects added into the queue.


    def __init__(self):
        """ Initialize the queue """
        self.queue = LinkedList()


    def enqueue(self, obj):
        """ Adds the object 'obj' at the end of the queue """
        #raise NotImplementedError("enqueue function is missing!")
        self.queue.add_last(obj)
        return True

    def dequeue(self):
        """ Removes and returns the first object in the queue """
        #raise NotImplementedError("dequeue function is missing!")
        if self.is_empty():
            return None
        else:
            first = self.queue.get_position(0)
            self.queue.remove_position(0)
            return first


    def first(self):
        """ Returns the first object in the queue """
        #raise NotImplementedError("first function is missing!")
        if self.is_empty():
            return None
        else:
            return self.queue.get_position(0)


    def last(self):
        """ Returns the last object in the queue """
        #raise NotImplementedError("last function is missing!")
        if self.is_empty():
            return None
        else:
            lastIndex = self.queue.get_size()-1
            return self.queue.get_position(lastIndex)


    def is_empty(self):
        """ Returns true if the queue is empty, otherwise false """
        #raise NotImplementedError("is_empty function is missing!")
        return self.queue.get_size() == 0

