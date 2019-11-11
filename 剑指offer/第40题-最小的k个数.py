class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        import heapq
        # 此方法时间复杂度为O(nlogk)
        if k < 1 or k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)

if __name__ == "__main__":
    a = [3, 2, 1, 4]
    print(Solution().GetLeastNumbers_Solution(a, 2))