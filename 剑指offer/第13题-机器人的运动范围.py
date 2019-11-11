class Solution:
    def movingCount(self, rows, cols, k):
        if rows < 0 or cols < 0 or k < 0:
            return 0
        markmatrix = [0]*(rows*cols)
        row, col = 0, 0
        n = self.movingCountCore(rows, cols, row, col, k, markmatrix)
        return n

    def movingCountCore(self, rows, cols, row, col, k, markmatrix):
        n = 0
        if self.check(rows, cols, row, col, k, markmatrix):
            markmatrix[row * cols + col] = True
            n = 1 + self.movingCountCore(rows, cols, row + 1, col, k, markmatrix) + \
                      self.movingCountCore(rows, cols, row - 1, col, k, markmatrix) + \
                      self.movingCountCore(rows, cols, row, col + 1, k, markmatrix) + \
                      self.movingCountCore(rows, cols, row, col - 1, k, markmatrix)
        return n

    def check(self, rows, cols, row, col, k, markmatrix):
        if row >= 0 and row < rows and col >= 0 and col < cols and \
                self.getDigitSum(row) + self.getDigitSum(col) <= k and not\
                markmatrix[row * cols + col]:
            return True
        return False

    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum

if __name__== "__main__":
    print(Solution().movingCount(3, 3, 2))
