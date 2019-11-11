class Solution:
    def Permutation(self, ss):
        length = len(ss)
        if length == 0:
            return []
        if length == 1:
            return [ss]
        res = []
        for i in range(length):
            t = self.Permutation(ss[:i] + ss[i + 1:])
            for j in t:
                if ss[i] + j not in res:
                    res.append(ss[i] + j)
        return res

    def Group(self, ss):
        length = len(ss)
        if length == 0:
            return []
        if length == 1:
            return [ss]
        res = []
        for i in range(length):
            res.append(ss[i])
            t = self.Group(ss[:i]+ss[i+1:])
            for j in t:
                if ''.join(sorted(ss[i] + j)) not in res:
                    res.append(ss[i] + j)
        return res

    def pl(self, ss):
        z = 'abcdefghijklmnopqrstuvwxyz'
        l = len(ss)
        a = z[:l]
        def px(a):
            length = len(a)
            if length == 0:
                return []
            if length == 1:
                return [a]
            res = []
            for i in range(length):
                t = px(a[:i] + a[i + 1:])
                for j in t:
                    if a[i] + j not in res:
                        res.append(a[i] + j)
            return res
        result = px(a)
        R = []
        for i in range(len(result)):
            res = result[i]
            re = list(res)
            r = []
            for i in range(len(re)):
                w = z.find(re[i])
                r.append(ss[w])
            if (r[0] + r[1] + r[2] + r[3] == r[4] + r[5] + r[6] + r[7] and \
                    r[0] + r[2] + r[4] + r[6] == r[1] + r[3] + r[5] + r[7] and \
                    r[0] + r[1] + r[4] + r[5] == r[2] + r[3] + r[6] + r[7]):
                R.append(r)
        return R







if __name__ == '__main__':
    a = [1, 1, 2, 2, 2, 2, 1, 1]
    b = Solution()
    print(b.pl(a))
