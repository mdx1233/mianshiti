class Solution:
    def FindGreatestSumOfSubArray(self, arr):
        if not arr or len(arr) < 1:
            return 0
        Sum = 0
        Greatnum = 0
        for i in range(len(arr)):
            if Sum <= 0:
                Sum = arr[i]
            else:
                Sum += arr[i]
            if Sum > Greatnum:
                Greatnum = Sum
        return Greatnum
    # 动态规划
    def FindGreatestSumOfSubArray1(self, arr):
        if not arr or len(arr) < 1:
            return 0
        alist = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0 or alist[i-1] <= 0:
                alist[i] = arr[i]
            else:
                alist[i] = arr[i] + alist[i-1]
        return alist, max(alist)

if __name__ == "__main__":
    a = [2, -3, 4, -1, -2, 6]
    print(Solution().FindGreatestSumOfSubArray1(a))
