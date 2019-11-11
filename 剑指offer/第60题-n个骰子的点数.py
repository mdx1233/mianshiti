class Solution:
    def PrintProbability(self, n):
        if n < 1:
            return
        maxVal = 6
        probStorage = [[0 for i in range(6 * n)] for i in range(n)]
        for i in range(maxVal):
            probStorage[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                probStorage[i][j] = probStorage[i - 1][j - 1] + probStorage[i - 1][j - 2] + probStorage[i - 1][j - 3] +\
                probStorage[i - 1][j - 4] + probStorage[i - 1][j - 5] + probStorage[i - 1][j - 6]
        count = probStorage[n - 1]
        p = [i/6**n for i in count]
        return count, p
if __name__ == '__main__':
    print(Solution().PrintProbability(3))
