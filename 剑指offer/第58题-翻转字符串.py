class Solution:
    def ReverseSentence(self, s):
        if not s or len(s) < 1:
            return
        s = self.Reverse(s)
        start = 0
        end = 0
        l = len(s)
        res = []
        while end < l:
            if s[end] == ' ':
                res.append(self.Reverse(s[start:end]))
                end += 1
                start = end
            elif end == l - 1:
                res.append(self.Reverse(s[start:]))
                break
            else:
                end += 1
        return ' '.join(res)


    def Reverse(self, s):
        l = len(s)
        first = 0
        last = l - 1
        res = [0]*l
        while first <= last:
            res[first] = s[last]
            res[last] = s[first]
            first += 1
            last -= 1
        return ''.join(res)

    def ReverseSentence1(self, s):
        if not s or len(s) < 1:
            return
        s = s[::-1]
        a = s.split(' ')
        for i in range(len(a)):
            a[i] = a[i][::-1]
        return ' '.join(a)
if __name__ == '__main__':
    s = 'I am a student.'
    print(Solution().ReverseSentence1(s))

