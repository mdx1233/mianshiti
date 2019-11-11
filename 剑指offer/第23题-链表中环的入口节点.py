class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

class Solution:
    def EntryNodeOfLoop(self, head):
        if not head:
            return None
        first = head
        second = head
        while first._next != second._next._next:
            first = first._next
            second = second._next._next
        print(first._next._value)
        first1 = first._next
        first2 = first._next
        n = 1
        while first1._next != first2:
            first1 = first1._next
            n += 1
        print('环中有', n, '个节点')
        third = head
        forth = head
        for i in range(n):
            third = third._next
            l = 1
        while forth != third:
            forth = forth._next
            third = third._next
            l += 1
        print('第', l, '个节点为环的入口节点,节点值为', forth._value)
        return forth

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1._next = node2
    node2._next = node3
    node3._next = node4
    node4._next = node5
    node5._next = node6
    node6._next = node7
    node7._next = node3
    nodedk = Solution().EntryNodeOfLoop(node1)
