class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None
        self.next = None

class Solution:
    def GetNext(self, node):
        if not node:
            return None
        # 如果该节点有右子树，那么下一个节点就是它右子树中的最左节点
        if node.rchild:
            node = node.rchild
            while node.lchild:
                node = node.lchild
            return node
        else:
            # 如果一个节点没有右子树，并且它还是它父节点的左子节点
            if node.next and node.next.lchild == node:
                return node.next
            # 如果一个节点没有右子树，并且它还是它父节点的右子节点
            else:
                node = node.next
                while node:
                    if node.next and node.next.lchild == node.next:
                        return node.next
                    else:
                        node = node.next
                return node


