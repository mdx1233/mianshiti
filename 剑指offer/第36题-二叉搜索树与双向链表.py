class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.b = []
        self.inorder(pRootOfTree)

        for i, j in enumerate(self.b[:-1]):
            self.b[i].rchild = self.b[i+1]
            self.b[i+1].lchild = j

        return self.b[0]
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.lchild)
        self.b.append(root)
        self.inorder(root.rchild)

class Solution1:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        root = pHead = pRootOfTree
        while pHead.lchild:
            pHead = pHead.lchild
        self.Core(root)
        return pHead


    def Core(self, root):
        if not root.lchild and root.rchild:
            return
        if root.lchild:
            preroot = root.lchild
            self.Core(root.lchild)
            while preroot.rchild:
                preroot = preroot.rchild
            preroot.rchild = root
            root.lchild = preroot
        if root.rchild:
            nextroot = root.rchild
            self.Core(root.rchild)
            while nextroot.lchild:
                nextroot = nextroot.lchild
            nextroot.lchild = root
            root.rchild = nextroot
if __name__ == '__main__':
    a = TreeNode(10)
    a.lchild = TreeNode(6)
    a.rchild = TreeNode(14)
    a.lchild.lchild = TreeNode(4)
    a.lchild.rchild = TreeNode(8)
    a.rchild.lchild = TreeNode(12)
    a.rchild.rchild = TreeNode(16)

    b = Solution1()
    print(b.Convert(a).rchild.lchild.elem)