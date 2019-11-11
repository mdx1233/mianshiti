class Solution: #时间复杂度为O(1)
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())

    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop()
        self.minstack.pop()

    def min(self):
        return self.minstack[-1]

if __name__ == '__main__':
    a = Solution()
    a.push(1)
    a.push(2)
    print(a.min())