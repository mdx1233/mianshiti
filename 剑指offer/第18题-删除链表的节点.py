class ListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class PrintNode():
  def print_node(self,node):
    res_list = []
    while node:
      res_list.append(str(node.value))
      node = node.next_node
    print('->'.join(res_list))



class Solution:
    def delete_node(self, head_node, del_node):
        """
        删除指定节点
        """
        if not (head_node and del_node):
            return False

        # 要删除的节点不是尾节点
        if del_node.next_node:
            del_next_node = del_node.next_node
            del_node.value = del_next_node.value
            del_node.next_node = del_next_node.next_node
            del_next_node.value = None
            del_next_node.next_node = None

        # 链表只要一个节点，删除头节点（也是尾节点）
        elif del_node == head_node:
            head_node = None
            del_node = None

        # 链表中有多个节点，删除尾节点
        else:
            node = head_node
            while node.next_node != del_node:
                node = node.next_node
            node.next_node = None
            del_node = None

        return head_node

if __name__ == '__main__':
  node1 = ListNode(90)
  node2 = ListNode(34)
  node3 = ListNode(89)
  node4 = ListNode(77)
  node5 = ListNode(23)
  node1.next_node = node2
  node2.next_node = node3
  node3.next_node = node4
  node4.next_node = node5
  printnode = PrintNode()
  printnode.print_node(node1)
  Solution().delete_node(node1, node5)
  printnode.print_node(node1)


