# if not a : if a == 0/[]/False/{}/None
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or rows < 0 or cols < 0 or path == None:
            return False
        markmatrix = [0]*(rows*cols)
        pathIndex = 0

        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathIndex, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathIndex, markmatrix):
        if pathIndex == len(path):
            return True
        hasPath = False
        if row >= 0 and row < rows and col >=0 and col < cols and matrix[row*cols+col] == path[pathIndex] and not markmatrix[row*cols+col]:
            pathIndex += 1
            markmatrix[row*cols+col] = True
            hasPath = self.hasPathCore(matrix, rows, cols, row+1, col, path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row-1, col,path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row, col+1, path, pathIndex, markmatrix) or \
                    self.hasPathCore(matrix, rows, cols, row, col-1, path, pathIndex, markmatrix)
            if not hasPath:
                pathIndex -= 1
                markmatrix[row*cols+col] = False
        return hasPath

if __name__== "__main__":
    l = ['a', 'b', 't', 'g', 'b', 'f', 'c', 's', 'j', 'd', 'e', 'h']
    print(Solution().hasPath(l,3,4,['a', 'b', 'j', 'd']))