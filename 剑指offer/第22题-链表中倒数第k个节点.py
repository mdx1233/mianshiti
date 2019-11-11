class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

class Solution:
    def FindKthToTail(self, head, k):
        if not head and k <= 0:
            return None
        first = head
        second = head
        for i in range(k-1):
            if first._next:
                first = first._next
            else:
                return None
        while first._next:
            first = first._next
            second = second._next
        return second

class Solution1:
    def FindKthToTail(self, head, k):
        if not head and k <= 0:
            return None
        first = head
        n = 1
        while first._next:
            first = first._next
            n += 1
        if k > n:
            return None
        second = head
        for i in range(n - k + 1):
            if second._next:
                second = second._next
                return second
            else:
                return None



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
    nodedk = Solution1().FindKthToTail(node1, 4)
    print(nodedk._value)