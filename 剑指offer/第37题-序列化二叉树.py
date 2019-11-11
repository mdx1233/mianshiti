class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Solution:
    flag = -1
    def Serialize(self, root):
        if root == None:
            return '#'
        result = root.elem
        l = self.Serialize(root.lchild)
        r = self.Serialize(root.rchild)
        return str(result) + ',' + l + ',' + r

    def Deserialize(self, s):
        self.flag += 1
        lis = s.split(',')

        if self.flag >= len(s):
            return None

        root = None
        if lis[self.flag] != '#':
            root = Node(int(lis[self.flag]))
            root.lchild = self.Deserialize(s)
            root.rchild = self.Deserialize(s)
        return root


if __name__ == '__main__':
    a = Node(10)
    a.lchild = Node(6)
    a.rchild = Node(14)
    a.lchild.lchild = Node(4)
    a.lchild.rchild = Node(8)
    a.rchild.lchild = Node(12)
    a.rchild.rchild = Node(16)
    s = '10,6,4,#,#,8,#,#,14,12,#,#,16,#,#'
    b = Solution()
    print(b.Serialize(a))
    print(b.Deserialize(s).rchild.elem)