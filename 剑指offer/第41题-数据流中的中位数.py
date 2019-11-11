from heapq import *
class Solution:
    def insertleft(self, left, right, x):
        return left.append(heappushpop(right, x))

    def insertright(self, right, left, x):
        left = [-i for i in left]
        x = -x
        return right.append(-1 * heappushpop(left, x))

    def GetMedian(self, arr):
        left = []
        right = []
        l = len(arr)
        for i in range(l):
            if i % 2 == 0:
                self.insertleft(left, right, arr[i])
            else:
                self.insertright(right, left, arr[i])
        left = [-i for i in left]
        heapify(left)
        heapify(right)
        if l % 2 == 1:
            median = -1 * heappop(left)
        else:
            median = 1/2 * (-1 * heappop(left) + heappop(right))
        return median

if __name__ == "__main__":
    a = [1, 2, 3, 5, 7, 4, 7, 8]
    print(Solution().GetMedian(a))
