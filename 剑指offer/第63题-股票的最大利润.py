class Solution:
    def MaxDiff(self, arr):
        if not arr or len(arr) < 1:
            return
        Min = arr[0]
        res = [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i-1] < Min:
                Min = arr[i-1]
            res[i] = arr[i] - Min
        return max(res)
if __name__ == '__main__':
    a = [9, 11, 8, 5, 7, 12, 16, 14]
    print(Solution().MaxDiff(a))