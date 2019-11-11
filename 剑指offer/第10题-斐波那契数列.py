#  n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)
# 循环实现
class Solution:
    def f(self, n):
        f0 = 0
        f1 = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        else:
            while n != 1:
                sum = f0 + f1
                f0 = f1
                f1 = sum
                n -= 1
            return sum

# 递归实现
class Solution1:
    def f(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.f(n-1) + self.f(n-2)

if __name__ == '__main__':
    print(Solution().f(2))
    print(Solution1().f(2))