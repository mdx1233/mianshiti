class Stack:
    def __int__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):   # 入栈： 把一个元素添加到栈的最顶层
        self.stack.append(item)

    def pop(self):      # 出栈：删除栈最顶层的元素，并返回这个元素
        if self.is_empty():
            raise (IndexError, 'pop from empty stack')
        return self.stack.pop()

    def peek(self):     # 返回最顶层的元素，并不删除它
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def IsPopOrder(self, pushV, popV):
        stack = []
        while popV:
            if stack and stack[-1] == popV[0]:
                    stack.pop()
                    popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True

if __name__ == '__main__':
    a = Stack()
    r = [1, 2, 3, 4, 5]
    c = [4, 3, 5, 1, 2]
    print(a.IsPopOrder(r, c))