class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class PrintNode():
  def print_node(self,node):
    res_list = []
    while node:
      res_list.append(str(node.value))
      node = node.next
    print('->'.join(res_list))



class Solution:
    def deleteDuplication(self, head):
        if head is None:
            return None
        cur = head
        while cur.next:
            if cur.value == cur.next.value:
                if cur.next.next is None:
                    cur.next.value = None
                    cur.next = None
                else:
                    temp = cur.next.next
                    cur.next = temp
            else:
                cur = cur.next

        return head




if __name__ == '__main__':
  node1 = ListNode(22)
  node2 = ListNode(22)
  node3 = ListNode(22)
  node4 = ListNode(23)
  node5 = ListNode(4)
  node1.next = node2
  node2.next = node3
  node3.next = node4
  node4.next = node5
  printnode = PrintNode()
  printnode.print_node(node1)
  Solution().deleteDuplication(node1)
  printnode.print_node(node1)