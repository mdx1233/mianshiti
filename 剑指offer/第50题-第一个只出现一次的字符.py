class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) < 0:
            return -1
        res = {}
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for i in s:
            if res[i] == 1:
                return i
    def delsame(self, s1, s2):
        if len(s1) < 0 or len(s2) < 0:
            return -1
        for i in s2:
            s1 = s1.replace(i, '')
        return s1

    def delsame1(self, s):
        if len(s) < 0:
            return -1
        res = {}
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for i in res:
            if res[i] != 1:
                s = s.replace(i, '')
        return s
    def issame(self, s1, s2):
        if len(s1) < 0 or len(s2) < 0:
            return -1
        res = {}
        for i in s1:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for i in s2:
            if i in res:
                res[i] -= 1
            else:
                res[i] = 1
        r = True
        for i in res:
            if res[i] != 0:
                r = r and False
            else:
                r = r and True
        return r
if __name__ == '__main__':
    s1 = 'listen'
    s2 = 'silent'
    print(Solution().issame(s1, s2))