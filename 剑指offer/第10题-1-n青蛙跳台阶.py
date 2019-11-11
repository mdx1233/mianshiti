# 一只青蛙一次可以跳上1级台阶，也可以跳上2级,一直到n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 数学归纳法
class Solution:
    def f(self, n):
        if n <= 0:
            print('error')
        return 2 ** (n-1)