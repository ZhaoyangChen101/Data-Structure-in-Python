# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ A class to describe a list node object
#​‌​​​​​‌‌‌​‌​​​ The node object has the following attributes: obj, follower and predecessor

class ListNode:
    """
    The LinkedList uses ListNode objects to store added values.
    This class will not be tested by the grader.

    Attributes:
      obj: Any object that needs to be stored.
      follower: A ListNode object that follows this (self) ListNode object
        in the linked list.
      predecessor: A ListNode object that precedes this (self) ListNode object
        in the linked list.
    """
    def __init__(self, obj):
        """Initialize a list node object with the value obj."""
        self.obj = obj
        self.follower = None
        self.predecessor = None

    def add_after(self, node):
        """Adds node 'node' as the follower of this node."""
        tmp = self.follower
        self.follower = node
        node.predecessor = self
        node.follower = tmp
        if tmp:
            tmp.predecessor = node

    def remove_after(self):
        """Removes the follower of this node."""
        if self.follower:
            self.follower = self.follower.follower
            if self.follower:
                self.follower.predecessor = self


class UnderflowError(Exception):
    """An error raised when trying to remove one of guardian nodes."""
    def __init__(self):
        super().__init__("Can't remove from an empty list!")


class LinkedList:
    """
    An implementation of a doubly linked list that uses ListNode objects
    to represent nodes in the list. List indexes start from zero.

    The list contains one head and one tail guardian node with the values None.
    These can be used to check if the head or tail has been reached.
    The guardian nodes should not be included when counting the size of the list.
    """
    def __init__(self):
        """Initialize the linked list."""
        self.ListNode = ListNode
        self.head = self.ListNode(None)
        self.tail = self.ListNode(None)
        #​‌​​​​​‌‌‌​‌​​​ An empty list should only have one head node followed by a tail node
        self.head.add_after(self.tail)

    def _get_at(self, n):
        """Return the node at position 'n'."""
        #raise NotImplementedError("_get_at not implemented")
        if n > self.get_size() or n < 0:
            return None
        else:
            node = self.head
            pos = -1
            while node.follower is not None:
                pos += 1
                if pos == n:
                    return node.follower
                else:
                    node = node.follower

    def add_first(self, obj):
        """Add the object 'obj' as the first node."""
        #raise NotImplementedError("add_first not implemented")
        oldFirst = self.head.follower
        newNode = ListNode(obj)
        #relation between obj and head
        self.head.follower = newNode
        newNode.predecessor = self.head
        #relation between obj and oldFirst
        newNode.follower = oldFirst
        oldFirst.predecessor = newNode
        return True

    def add_last(self, obj):
        """Add the object 'obj' as the last node."""
        #raise NotImplementedError("add_last not implemented")
        oldLast = self.tail.predecessor
        newNode = ListNode(obj)
        # relation between obj and oldLast
        oldLast.follower = newNode
        newNode.predecessor = oldLast
        # relation between obj and tail
        newNode.follower = self.tail
        self.tail.predecessor = newNode
        return True

    def add_position(self, n, obj):
        """Insert the object 'obj' as the 'n'th node."""
        #raise NotImplementedError("add_position not implemented")
        newNode = ListNode(obj)
        if n >=0 & n <= self.get_size():
            curr = self._get_at(n)
            if curr is not None:
                first = curr.predecessor
                # relation between curr and first
                first.follower = newNode
                newNode.predecessor = first
                # relation between obj and curr
                newNode.follower = curr
                curr.predecessor = newNode
                return True
            else:
                return False
        else:
            return False

    def remove_position(self, n):
        """Remove the node at the 'n'th position."""
        node_at_n = self._get_at(n)
        #​‌​​​​​‌‌‌​‌​​​Prevent from removing guardian nodes.
        if node_at_n is self.tail or node_at_n is self.head:
            raise UnderflowError()

        predecessor = node_at_n.predecessor
        if predecessor:
            predecessor.remove_after()

    def get_position(self, n):
        """Return the value of the node at the 'n'th position or None
        if there is no node at that position."""
        node = self._get_at(n)
        return node.obj if node else None

    def get_size(self):
        """Return the number of objects in the list."""
        #raise NotImplementedError("get_size not implemented")
        if self.head.follower == self.tail:
            return 0
        else:
            node = self.head
            size = 0
            while node.follower is not self.tail:
                size += 1
                node = node.follower
            return size
    def get_max(self):
        """Return the value of the largest node in the list."""
        #raise NotImplementedError("get_max not implemented")
        node = self.head.follower
        max = node.obj
        while node.follower is not self.tail:
            currValue = node.follower.obj
            if max < currValue:
                max = currValue
            node = node.follower
        return max



