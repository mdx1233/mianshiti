class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Solution:
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = []
        def FindPathCore(root, path, currentNum):
            currentNum += root.elem
            path.append(root)

            flag = (root.lchild == None and root.rchild == None)  # 判断是否达到叶子节点

            if currentNum == expectNumber and flag:  # 如果到达叶子节点且当前值等于期望值
                onepath = []
                for node in path:
                    onepath.append(node.elem)
                result.append(onepath)

            if currentNum < expectNumber:
                if root.lchild:
                    FindPathCore(root.lchild, path, currentNum)
                if root.rchild:
                    FindPathCore(root.rchild, path, currentNum)
            path.pop()

        FindPathCore(root, [], 0)
        return result
if __name__ == '__main__':
    a = Node(10)
    a.lchild = Node(5)
    a.rchild = Node(12)
    a.lchild.lchild = Node(4)
    a.lchild.rchild = Node(7)

    b = Solution()
    print(b.FindPath(a, 22))
