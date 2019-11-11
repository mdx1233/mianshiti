class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.elem == pRoot2.elem:
                res = self.SubtreeCore(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.lchild, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.rchild, pRoot2)
        return res

    def SubtreeCore(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.elem != pRoot2.elem:
            return False
        return self.SubtreeCore(pRoot1.lchild, pRoot2.lchild) and self.SubtreeCore(pRoot1.rchild, pRoot2.rchild)
