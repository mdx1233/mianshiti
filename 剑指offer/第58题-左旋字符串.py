class Solution:
    def LeftRotateString(self, s, k):
        if not s or len(s) < 1 or k < 0:
            return
        r = []
        r.append(s[:k][::-1])
        r.append(s[k:][::-1])
        return ''.join(r)[::-1]

if __name__ == '__main__':
    s = 'abcdefg'
    print(Solution().LeftRotateString(s, 2))