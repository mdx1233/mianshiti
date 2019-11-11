# 利用Python特性
class Solution:
        def NumberOf1(self, n):
            return bin(n & 0xffffffff).count('1')

# 最佳方法：把一个整数减去1，再和原整数做“与运算”，会把该整数最右边的1变成0。那么一个整数的二进制中表示中有多少个1，就可以进行多少次这样的操作。
class Solution1:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = (n-1) & n
            count += 1
        return count


