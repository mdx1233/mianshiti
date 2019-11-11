class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Solution:
    def KthNode(self, pRoot, k):
        if not pRoot or k < 1:
            return None
        res = []

        def inorder1(pRoot):
            if not pRoot:
                return []
            inorder1(pRoot.lchild)
            res.append(pRoot)
            inorder1(pRoot.rchild)
        inorder1(pRoot)
        return res[k - 1]
    def inorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        l = self.inorder(root.lchild)
        r = self.inorder(root.rchild)
        return l + result + r


    
if __name__ == '__main__':
    a = Node(5)
    a.lchild = Node(3)
    a.rchild = Node(7)
    a.lchild.lchild = Node(2)
    a.lchild.rchild = Node(4)
    a.rchild.lchild = Node(6)
    a.rchild.rchild = Node(8)
    print(Solution().KthNode(a, 4).elem)