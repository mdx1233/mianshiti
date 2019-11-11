class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        left = self.TreeDepth(pRoot.lchild)
        right = self.TreeDepth(pRoot.rchild)
        return max(left, right) + 1

if __name__ == '__main__':
    a = Node(1)
    a.lchild = Node(2)
    a.rchild = Node(3)
    a.lchild.lchild = Node(4)
    a.lchild.rchild = Node(5)
    a.rchild.rchild = Node(6)
    a.lchild.rchild.lchild = Node(7)
    print(Solution().TreeDepth(a))