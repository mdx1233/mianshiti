class solution:
    def replaceSpace(self,s):
        return s.replace(' ','%20')

class solution1:
    def replaceSpace(self,s):
        return '%20'.join(s.split(' ')) # join():连接函数 str.join(sequence) sequence:要连接的元素序列

class solution2:
    def replaceSpace(self,s):
        s = list(s)
        for i, c in enumerate(s):
            if c == ' ':
                s[i] = '%20'
        return ''.join(s)

# 官方答案:从后往前
class solution3:
    def replaceSpace(self,s):
        s = list(s)
        n = 0
        for i in s:
            if i == ' ':
                n += 1
        p1 = len(s) - 1
        s += [None] * (n * 2)
        p2 = len(s) - 1
        while p1 >= 0:
            if s[p1] == ' ':
                for i in ['0','2','%']:
                    s[p2] = i
                    p2 -= 1
            else:
                s[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s)



if __name__== "__main__":
    l = 'We are happy'
    print(solution().replaceSpace(l))