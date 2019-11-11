class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        pMergedHead = None
        if pHead1._value < pHead2._value:
            pMergedHead = pHead1
            pMergedHead._next = self.Merge(pHead1._next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead._next = self.Merge(pHead1, pHead2._next)
        return pMergedHead

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1._next = node3
    node2._next = node4
    node3._next = node5
    node4._next = node6
    Solution().Merge(node1, node2)
    N = node1
    r = []
    while N:
        r.append(N._value)
        N = N._next
    print(r)
