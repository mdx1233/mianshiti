class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
        self._random = None
class Solution:
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.first_step(pHead)
        self.second_step(pHead)
        return self.third_step(pHead)

    def first_step(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = Node(0)
            pCloned._value = pNode._value
            pCloned._next = pNode._next
            pNode._next = pCloned
            pNode = pCloned._next

    def second_step(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode._next
            if pNode._random != None:
                pCloned._random = pNode._random.next
            pNode = pCloned._next

    def third_step(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode._next
        pNode._next = pClonedNode._next
        pNode = pNode._next
        while pNode:
            pClonedNode._next = pNode._next
            pClonedNode = pClonedNode._next
            pNode._next = pClonedNode._next
            pNode = pNode._next
        return pClonedHead
