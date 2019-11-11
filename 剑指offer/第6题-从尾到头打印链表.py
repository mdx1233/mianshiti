# 先定一个Node的类
class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

# 创建单链表，并实现其应有功能
class SingleLinkList:
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):     # 判断是否为空
        return  self._head == None

    def length(self):       # 链表长度
        c = self._head
        n = 0
        while c != None:
            n += 1
            c = c._next
        return n

    def travel(self):
        c = self._head
        while c != None:
            print(c._value, end=' ')
            c = c._next
        print('\n')

    def add(self, value):       # 在链表头部添加元素
        newnode = Node(value)
        newnode._next = self._head
        self._head = newnode

    def append(self, value):    # 在链表尾部添加元素
        newnode = Node(value)
        if self.is_empty():     # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
            self._head = newnode
        else:
            c = self._head
            while c._next != None:
                c = c._next
            c._next = newnode

    def insert(self, pos, value):       # 在链表任意位置添加元素
        if pos <= 0:         # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(value)
        elif pos > self.length() - 1:
            self.append(value)      # 如果pos位置比原链表长，那么都当做尾插法来做
        else:
            c = self._head
            count = 0
            while count < pos - 1:      # 推出循环时，c指向pos-1的位置
                count += 1
                c = c._next
            newnode = Node(value)
            newnode._next = c._next
            c._next = newnode

    def remove(self, value):        # 删除节点
        c = self._head
        p = None
        while c != None:
            if c._value == value:
                if c == self._head:
                    self._head = c._next
                else:
                    p._next = c._next
                    break
            else:
                p = c
                c = c._next

    def search(self, value):
        c = self._head
        while c != None :
            if c._value == value:
                return True
            else:
                c = c._next
        return False


    def printListFromTailToHead(Node):
        ls = []
        while Node != None:
            ls.append(Node._value)
            Node = Node._next
        return ls[::-1]

    if __name__ == '__main__':
        node = Node(1)
        node._next = Node(2)
        print(printListFromTailToHead(node))