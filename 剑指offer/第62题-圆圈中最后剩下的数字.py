class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        res = 0
        for i in range(2, n+1):
            res = (res+m) % i
        return res

class Solution1:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        l = [i for i in range(n)]

        j = 0
        while len(l) > 1:
            j = (j + m - 1) % len(l)
            l.remove(l[j])

        return l[0]

if __name__ == '__main__':
    n = 5
    m = 3
    print(Solution().LastRemaining_Solution(n, m))
