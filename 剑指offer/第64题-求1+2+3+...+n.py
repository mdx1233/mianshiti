class Solution:
    def Sum_Solution(self, n):
        return self.sum(n)

    def sum0(self, n):
        return 0

    def sum(self, n):
        func = {False: self.sum0, True: self.sum}
        return n + func[not not n](n - 1)


if __name__ == '__main__':
    n = 5
    print(Solution().sum(n))