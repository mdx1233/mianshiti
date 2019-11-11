class Solution:
    def NumOnlyAppearOnce(self, arr):
        if not arr or len(arr) < 1:
            return []
        arrbin = []
        for i in arr:
            arrbin.append(bin(i)[2:])
        print(arrbin)
        l = 0
        for i in arrbin:
            l = max(l, len(i))
        res = [0]*l

        for i in range(l):
            for j in arrbin:
                if len(j) > i:
                    res[l-i-1] += int(j[len(j)-i-1])
                else:
                    res[l-i-1] += 0
                print(res)
        su = 0
        for i in range(l):
            if res[i] % 3 != 0:
                su += 2 ** (l-i-1)
        return su

if __name__ == '__main__':
    a = [1, 2, 2, 2, 3, 3, 3]
    print(Solution().NumOnlyAppearOnce(a))
