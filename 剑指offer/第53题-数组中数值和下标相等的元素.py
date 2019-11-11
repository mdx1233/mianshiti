class Solution:
    def GettNumberSameAsIndex(self, arr):
        if not arr or len(arr) < 1:
            return
        l = len(arr)
        start = 0
        end = l - 1
        while end >= start:
            mid = (end + start) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] > mid:
                end = mid - 1
            else:
                start = mid + 1

if __name__ == '__main__':
    a = [-3, -1, 1, 3, 5]
    print(Solution().GettNumberSameAsIndex(a))