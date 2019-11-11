class Solution:
    def FindNumbersWithSum(self, arr, s):
        if not arr or len(arr) < 2 or not s:
            return
        first = 0
        last = len(arr) - 1
        res = []
        while first < last:
            if arr[first] + arr[last] == s:
                res.append([arr[first], arr[last]])
                first += 1
                last -= 1
            elif arr[first] + arr[last] < s:
                first += 1
            else:
                last -= 1
        return res

if __name__ == '__main__':
    a = [1, 2, 4, 7, 11, 15]
    s = 15
    print(Solution().FindNumbersWithSum(a, s))