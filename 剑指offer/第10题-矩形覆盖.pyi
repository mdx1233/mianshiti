# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 循环实现
class Solution:
    def f(self, n):
        f1 = 1
        f2 = 2
        if n <= 0:
            print('error')
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            while n != 2:
                sum = f1 + f2
                f1 = f2
                f2 = sum
                n -= 1
            return sum

# 递归实现
class Solution1:
    def f(self, n):
        if n <= 0:
            print('error')
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.f(n-1) + self.f(n-2)

if __name__ == '__main__':
    print(Solution().f(2))
    print(Solution().f(2))