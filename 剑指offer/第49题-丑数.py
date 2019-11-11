class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        n = 0
        uglyn  = 0
        while uglyn < index:
            n += 1
            if self.isugly(n):
                uglyn += 1
        return n

    def isugly(self, n):
        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5
        return True if n == 1 else False

    def GetUglyNumber_Solution1(self, index):
        if index <= 0:
            return 0
        res = [1]
        T2 = T3 = T5 = 0
        uglyn = 1
        while uglyn < index:
            min_val = min(res[T2] * 2, res[T3] * 3, res[T5] * 5)
            res.append(min_val)
            while res[T2] * 2 <= min_val:
                T2 += 1
            while res[T3] * 3 <= min_val:
                T3 += 1
            while res[T5] * 5 <= min_val:
                T5 += 1
            uglyn += 1
        return res[-1]

if __name__ == '__main__':
    index = 15
    print(Solution().GetUglyNumber_Solution1(index))