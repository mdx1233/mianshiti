class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalCore(pRoot, pRoot)

    def isSymmetricalCore(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.elem != pRoot2.elem:
            return False
        return self.isSymmetricalCore(pRoot1.lchild, pRoot2.rchild) and self.isSymmetricalCore(pRoot1.rchild, pRoot2.lchild)