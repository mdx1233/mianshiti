class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence or len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:  # 找出左小右大的分界点i,此时i属于右子树
            if node > root:
                break
            i += 1
        for node in sequence[i:-1]:  # 如果在右子树中有比根节点小的值，直接返回False
            if node < root:
                return False
        left = True  # 判断左子树是否为二叉搜索树
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True  # 判断右子树是否为二叉搜索树
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right


if __name__ == '__main__':
    cs = [5, 7, 6, 9, 11, 10, 8]
    print(Solution().VerifySquenceOfBST(cs))