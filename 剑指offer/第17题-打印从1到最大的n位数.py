class Solution:
    def printmax1_n(self, n):
        r = []
        l = 10 ** n
        for i in range(1, l):
            r.append(i)
        return r

if __name__ == '__main__':
    print(Solution().printmax1_n(2))