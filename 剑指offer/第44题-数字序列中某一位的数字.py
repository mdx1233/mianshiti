class Solution:
    def digitAtIndex(self, n):
        if n < 0:
            return
        if n < 10:
            return n
        i = 0
        c = n
        while c > 0:
            c -= (i+1) * 9 * 10 ** i
            i += 1
        if c == 0:
            return 9
        k = c + i * 9 * 10 ** (i - 1)
        g = k // i
        w = k % i
        if w == 0:
            r = str(10 ** (i-1) + g - 1)[-1]
        else:
            r = str(10 ** (i-1) + g)[w - 1]
        return r

if __name__ == "__main__":
    a = 1001
    print(Solution().digitAtIndex(a))
