class Solution:
    def GetMissingNumber(self, arr):
        if not arr or len(arr) < 1:
            return
        l = len(arr)
        start = 0
        end = l - 1
        while end >= start:
            mid = (end + start) // 2
            if arr[mid] != mid:
                if (mid > 0 and arr[mid - 1] == mid - 1) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1

if __name__ == '__main__':
    n = 5
    a = []
    for i in range(n):
        a.append(i)
    a.pop(2)
    print(Solution().GetMissingNumber(a))


