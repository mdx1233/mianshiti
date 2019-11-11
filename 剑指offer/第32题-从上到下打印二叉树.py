# 节点类
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Solutiuon:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        r = []
        res.append(root)
        while len(res) > 0:
            node = res.pop(0)
            r.append(node.elem)
            if node.lchild:
                res.append(node.lchild)
            if node.rchild:
                res.append(node.rchild)
        return r

    def Print(self, root):
        if not root:
            return []
        res = []
        r = []
        res.append(root)
        nextLevel = 0    # 表示下一层节点的数目
        toBePrinted = 1    # 表示当前层还没有打印的节点数
        temp = []
        while len(res) > 0:
            node = res.pop(0)
            temp.append(node.elem)
            if node.lchild:
                res.append(node.lchild)
                nextLevel += 1
            if node.rchild:
                res.append(node.rchild)
                nextLevel += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                r.append(temp)
                toBePrinted = nextLevel
                nextLevel = 0
                temp = []
        return r

    def Print1(self, root):
        if not root:
            return []
        res = []
        r = []
        res.append(root)
        nextLevel = 0    # 表示下一层节点的数目
        toBePrinted = 1    # 表示当前层还没有打印的节点数
        cs = 1
        temp = []
        while len(res) > 0:
            node = res.pop(0)
            temp.append(node.elem)
            if node.lchild:
                res.append(node.lchild)
                nextLevel += 1
            if node.rchild:
                res.append(node.rchild)
                nextLevel += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                if cs % 2 == 0:
                    temp.reverse()
                r.append(temp)
                toBePrinted = nextLevel
                nextLevel = 0
                temp = []
                cs += 1
        return r

    def Print2(self, root):
        if not root:
            return []
        res = []
        res.append(root)
        result = []
        while res:
            r = []
            re = []
            for node in res:
                r.append(node.elem)
                if node.lchild:
                    re.append(node.lchild)
                if node.rchild:
                    re.append(node.rchild)
            result.append(r)
            res = re
        return result



if __name__ == '__main__':
    a = Node(8)
    a.lchild = Node(6)
    a.rchild = Node(10)
    a.lchild.lchild = Node(5)
    a.lchild.rchild = Node(7)
    a.rchild.lchild = Node(9)
    a.rchild.rchild = Node(11)
    b = Solutiuon()
    print(b.Print2(a))
