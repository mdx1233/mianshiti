class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # 思路：前序结果可以确定树根节点，通过树根节点可以将中序切成左右两半
        if(len(pre) == 0):
            return None
        root = Node(pre[0])
        tin_root_index = tin.index(root.elem)
        self.reConstructBinaryTree(pre[1: tin_root_index+1], tin[0: tin_root_index])
        self.reConstructBinaryTree(pre[tin_root_index+1:], tin[tin_root_index+1:])
        return root


if __name__ == '__main__':
    p = [1,2,4,7,3,5,6,8]
    t = [4,7,2,1,5,3,8,6]
    Root = Solution().reConstructBinaryTree(p,t)
