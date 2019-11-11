# a的n次方
class Solution:
    def Power(self, a, n):
        if n == 0 and a == 0:
            r = '无意义'
            return r
        if n == 0 and a:
            return 1
        if n and a == 0:
            return 0
        if n < 0:
            return 1/self.power_p(a, n)
        if n > 0:
            return self.power_p(a, n)

    def power_p(self, a , n):
            n = abs(n)
            r = 1
            while n > 0:
                r = r * a
                n = n - 1
            return r
class Solution1:
    def Power(self, a, n):
        if n == 0 and a == 0:
            r = '无意义'
            return r
        if n == 0 and a:
            return 1
        if n and a == 0:
            return 0
        if n < 0:
            return 1 / self.power_p(a, n)
        if n > 0:
            return self.power_p(a, n)

    def power_p(self, a, n):
        n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return a
        r = self.power_p(a, n//2)
        if n % 2 == 0:
            r = r*r
        if n % 2 == 1:
            r = r*r*a
        return r


if __name__ == '__main__':
    print(Solution().Power(0, 0))
    print(Solution().Power(0, 2))
    print(Solution().Power(2, 0))
    print(Solution().Power(2, -2))
    print(Solution().Power(2, 2))
    print(Solution1().Power(0, 0))
    print(Solution1().Power(0, 2))
    print(Solution1().Power(2, 0))
    print(Solution1().Power(2, -2))
    print(Solution1().Power(2, 2))
