# 解题代码一：二层遍历
class solution:
    def find(self,list,number):
        m, n = len(list), len(list[0])
        for i in range(m):
            for j in range(n):
                if list[i][j] == number:
                    return True
        return False

# 解题代码二：从右上角或左下角开始
class solution1:
    def find(self,list,number):
        m, n = len(list), len(list[0])
        x = 0
        y = n-1
        while (x < m and y >= 0):
            if list[x][y] < number:
                x = x + 1
            elif list[x][y] > number:
                y = y - 1
            else:
                return True
        return False

if __name__== "__main__":
    l = [[1, 2, 8, 9],[2, 4, 9, 2],[4, 7, 10, 13],[6, 8, 11, 15]]
    print(solution1().find(l,20))