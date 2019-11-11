class Solution:
    def IsContinuous(self, arr):
        if not arr or len(arr) != 5:
            return
        res = []
        for i in arr:
            if i == 'A':
                res.append(1)
            elif i == 'J':
                res.append(11)
            elif i == 'Q':
                res.append(12)
            elif i == 'K':
                res.append(13)
            elif i == 'W':
                res.append(0)
            else:
                res.append(i)

        res.sort()
        k = 0
        w = 0
        for i in range(4):
            if res[i] == 0:
                w += 1
            else:
                k += res[i + 1] - res[i] - 1
        if w >= k:
            return True
        else:
            return False
if __name__ == '__main__':
    a = ['Q', 'W', 9, 10, 7]
    print(Solution().IsContinuous(a))

