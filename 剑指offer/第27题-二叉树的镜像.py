class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        temp = root.lchild
        root.lchild = root.rchild
        root.rchild = temp
        if root.lchild:
            self.Mirror(root.lchild)
        if root.rchild:
            self.Mirror(root.rchild)