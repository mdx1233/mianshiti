class Solution:
    # 动态规划
    def max1(self, l):
        if l < 2:
            return 0
        if l == 2:
            return 1
        if l == 3:
            return 2
        r = [0, 1, 2, 3]
        for i in range(4,l+1):
            max = 0
            for j in range(1, l//2+1):
                v = r[j] * r[i-j]
                if v > max:
                    max = v
            r.append(max)
        return r[l]

    # 贪婪算法
    def max2(self, l):
        if l < 2:
            return 0
        if l == 2:
            return 1
        if l == 3:
            return 2
        timesOf3 = l // 3
        if l - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timesOf2 = (l - timesOf3 * 3) // 2
        return (3 ** timesOf3) * (2 ** timesOf2)


if __name__=="__main__":
    print(Solution().max1(5))
    print(Solution().max2(5))