class Solution:
    def getMaxValue1(self, arr):
        rows = len(arr)  # 行数
        cols = len(arr[0])  # 列数
        if not arr or rows <= 0 or cols <= 0:
            return 0
        maxValues = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[i - 1][j]
                if j > 0:
                    left = maxValues[i][j - 1]
                maxValues[i][j] = max(up, left) + arr[i][j]
        return maxValues[rows - 1][cols - 1]

    def getMaxValue2(self, arr):
        rows = len(arr)  # 行数
        cols = len(arr[0])  # 列数
        if not arr or rows <= 0 or cols <= 0:
            return 0
        maxValues = [0 for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[j]
                if j > 0:
                    left = maxValues[j - 1]
                maxValues[j] = max(up, left) + arr[i][j]
        return maxValues[cols - 1]

if __name__ == '__main__':
    a = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(Solution().getMaxValue2(a))