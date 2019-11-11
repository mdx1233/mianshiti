# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
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