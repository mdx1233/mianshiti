class Solution:

    def __init__(self):
        self.char_dict = {}

    def FirstAppearingOnce(self):
        for i in self.char_dict:
            if self.char_dict[i] == 1:
                return i
        return '#'


    def Insert(self, char):
        if char not in self.char_dict:
            self.char_dict[char] = 1
        else:
            self.char_dict[char] = 2


if __name__ == '__main__':
    a = Solution()
    s = 'google'
    for i in range(len(s)):
        a.Insert(s[i])
        print(a.FirstAppearingOnce())