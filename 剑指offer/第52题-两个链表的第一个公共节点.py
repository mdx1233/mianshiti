class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next
class SingleLinkList:
    def __init__(self, node = None):
        self._head = node
    def is_empty(self):     # 判断是否为空
        return  self._head == None
    def append(self, value):    # 在链表尾部添加元素
        newnode = Node(value)
        if self.is_empty():     # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
            self._head = newnode
        else:
            c = self._head
            while c._next != None:
                c = c._next
            c._next = newnode
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        l1 = self.getlength(pHead1)
        l2 = self.getlength(pHead2)
        if l1 > l2:
            headlong = pHead1
            headshort = pHead2
        else:
            headlong = pHead2
            headshort = pHead1
        l = abs(l1 - l2)
        while l > 0:
            headlong = headlong._next
            l -= 1
        while headlong != None and headshort != None and self.issame(headlong, headshort) == False:
            headlong = headlong._next
            headshort =headshort._next
        return headlong


    def getlength(self, pHead):
        l = 0
        while pHead:
            pHead = pHead._next
            l += 1
        return l

    def issame(self, pHead1, pHead2):
        if self.getlength(pHead1) == self.getlength(pHead2):
            while pHead1 != None and pHead2 != None:
                if pHead1._value == pHead2._value:
                    pHead1 = pHead1._next
                    pHead2 = pHead2._next
                else:
                    return False
        return True

if __name__ == '__main__':
    head1 = Node(1)
    head1._next = Node(2)
    head1._next._next = Node(3)
    head1._next._next._next = Node(6)
    head1._next._next._next._next = Node(7)
    head2 = Node(4)
    head2._next = Node(5)
    head2._next._next = Node(6)
    head2._next._next._next = Node(7)
    print(Solution().FindFirstCommonNode(head1, head2)._value)