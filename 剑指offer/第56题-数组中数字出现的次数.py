class Solution:
    def FindNumsAppearOnce(self, arr):
        if not arr or len(arr) < 1:
            return []
        resultEOR = 0
        for i in arr:
            resultEOR = resultEOR ^ i

        index = self.FindFirstBit(resultEOR)

        res1, res2 = 0, 0
        for j in arr:
            if self.IsBit(j, index):
                res1 ^= j
            else:
                res2 ^= j
        return [res1, res2]

    def FindFirstBit(self, num):
        '''
        用于在整数num的二进制表示中找到最右边是1的位
        '''
        indexBit = 0
        while (num & 1 == 0 and indexBit < 32):
            num = num >> 1
            indexBit += 1
        return indexBit

    def IsBit(self, num, indexBit):
        '''
        用于判断在num的二进制表示中从右边起的indexBit位是否为1
        '''
        num = num >> indexBit
        return (num & 1)