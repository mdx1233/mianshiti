# 1.队列为空：当两个栈都为空的时候，队列为空
# 2.入对操作：入栈1
# 3.出队操作：当两个栈都为空的时候，引发错误“队为空”；
# 当栈2为空的时候，就将栈1的元素出栈然后入栈到栈2，然后栈2出栈即可。
# 当栈2不为空的时候，栈2出栈即可。

class Solution:
    def __init__(self):
        self.pushstack = []
        self.popstack = []

    def push(self, item):
        self.pushstack.append(item)

    def pop(self):
        if self.popstack:
            return self.popstack.pop()
        else:
            if not self.pushstack:
                print('Nothing to pop!')
                return None
            else:
                while self.pushstack:
                    self.popstack.append(self.pushstack.pop())
                return self.popstack.pop()

if __name__=='__main__':
    a = Solution()
    a.push(1)
    a.push(7)
    a.push(3)
    a.push(5)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())