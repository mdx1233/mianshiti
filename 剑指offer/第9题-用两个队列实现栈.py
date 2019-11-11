# 1.栈为空：当两个队列都为空的时候，栈为空
# 2.入栈操作：当队列2为空的时候，将元素入队到队列1；当队列1位空的时候，将元素入队到队列2；如果队列1和队列2 都为空的时候，那就选择入队到队列1.
# 3.出栈操作：当两个队列都为空的时候，引发错误“栈为空”；
# 当队列2位空的时候，如果队列1中只有一个元素，则直接将队列1中的元素出队；
# 如果队列1不止一个元素的时候，就将队列1的元素出队然后入队到队列2，知道队列1中只有一个元素，然后将队列1中的元素出队即可。
# 当队列1位空的时候，如果队列2中只有一个元素，则直接将队列2中的元素出队；
# 如果队列2不止一个元素的时候，就将队列2的元素出队然后入队到队列1，知道队列2中只有一个元素，然后将队列2中的元素出队即可。

class Solution:
    def __init__(self):
        self.pushqueue = []
        self.popqueue = []

    def push(self, item):
        if self.popqueue:
            self.popqueue.append(item)
        else:
            self.pushqueue.append(item)


    def pop(self):
        if self.popqueue:
            n = len(self.popqueue)
            while n > 1:
                self.pushqueue.append(self.popqueue.pop(0))
                n -= 1
            return self.popqueue.pop()
        else:
            if not self.pushqueue:
                print('Nothing to pop!')
                return None
            else:
                n = len(self.pushqueue)
                while n > 1:
                    self.popqueue.append(self.pushqueue.pop(0))
                    n -= 1
                return self.pushqueue.pop()

if __name__=='__main__':
    a = Solution()
    a.push(1)
    a.push(7)

    print(a.pop())
    a.push(3)
    print(a.pop())
