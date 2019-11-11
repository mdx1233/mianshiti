class Solution:
    def FinfContinuousSequence(self, s):
        if not s:
            return
        small = 1
        big = 2
        res = []
        while small < (s + 1)/2:
            if self.SUM(small, big) == s:
                r = []
                for i in range(small, big + 1):
                    r.append(i)
                res.append(r)
                big += 1
            elif self.SUM(small, big) < s:
                big += 1
            else:
                small += 1
        return res

    def SUM(self, small, big):
        su = 0
        for i in range(small, big + 1):
            su += i
        return su

class Solution1:
    def FinfContinuousSequence(self, s):
        if not s:
            return
        small = 1
        big = 2
        res = []
        su = 3
        while small < (s + 1)/2:
            if su == s:
                r = []
                for i in range(small, big + 1):
                    r.append(i)
                res.append(r)
                big += 1
                su += big
            elif su < s:
                big += 1
                su += big
            else:
                su -= small
                small += 1

        return res

if __name__ == '__main__':
    s = 9
    print(Solution1().FinfContinuousSequence(s))
