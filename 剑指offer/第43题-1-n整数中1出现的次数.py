class Solution:
    def NumberOf1Between1AndN(self, n):
        num = 0
        i = 1
        while i <= n:
            num += self.Numberof1(i)
            i += 1
        return num

    def Numberof1(self, i):
        n = 0
        while i > 0:
            if i % 10 == 1:
                n += 1
            i = i // 10
        return n

class Solution1:
    def get_1_nums(self, n):
        i = 1
        num = 0
        while i <= n:
            for j in str(i):
                if j == '1':
                    num += 1
            i += 1
        return num

# f(1) = 1
# f(2) = 9 * f(1) + 10 ** 1
# f(3) = 9 * f(2) + 10 ** 2
# f(n) = 9 * f(n-1) + 10 ** (n-1)
class Solution2:
    def get_1_nums(self, n):
        if n <= 0:
            return 0
        digit = self.get_digits(n)
        low_nums = self.get_1_digits(digit - 1)
        high = int(str(n)[0])   # 最高位
        low = n - high * 10 ** (digit - 1)  # 低位

        if high == 1:
            high_nums = low + 1
            all_nums = high_nums
        else:
            high_nums = 10 ** (digit - 1)
            all_nums = high_nums + low_nums * (high - 1)   # 34567,最高位大于1，要计算每个多位数后面包含的1（10000-19999，20000-29999）
        return low_nums + all_nums + self.get_1_nums(low)

    def get_digits(self, n):
        return len(str(n))

    def get_1_digits(self, d):
        if d <= 0:
            return 0
        if d == 1:
            return 1
        current = 9 * self.get_1_digits(d - 1) + 10 ** (d - 1)
        return self.get_1_digits(d - 1) + current



if __name__ == "__main__":
    a = 9923446
    import time
    t = time.clock()
    print(Solution().NumberOf1Between1AndN(a))
    print(time.clock() - t)
    t1 = time.clock()
    print(Solution1().get_1_nums(a))
    print(time.clock() - t1)
    t2 = time.clock()
    print(Solution2().get_1_nums(a))
    print(time.clock() - t2)