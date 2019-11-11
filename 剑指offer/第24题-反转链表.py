class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next
class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead._next:
            return pHead
        pPrev = None
        while pHead:
            temp = pHead._next
            pHead._next = pPrev
            pPrev = pHead
            pHead = temp
        return pPrev

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1._next = node2
    node2._next = node3
    node3._next = node4
    node4._next = node5
    h = Solution().ReverseList(node1)
    print(h._value)