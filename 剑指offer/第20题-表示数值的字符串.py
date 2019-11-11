class Solution:
    def isNumeric(self, s):
        if not s or len(s) <= 0:
            return False
        if ('e' in s) or ('E' in s):
            if s.count('e') + s.count('E') == 1:
                index1 = s.find('e')
                index2 = s.find('E')
                index = max(index1, index2)
                front = s[:index]
                behind = s[index + 1:]
                if '.' in behind or len(behind) == 0:
                    return False
                isfront = self.isDigit(front)
                isbehind = self.isDigit(behind)
                return isfront and isbehind
            else:
                return False

        else:
            return self.isDigit(s)

    def isDigit(self, s):
        n = 0
        allow_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        for i in range(len(s)):
            if s[i] not in allow_num:
                return False
            if s[i] == '.':
                n += 1
            if s[i] in '+-' and i != 0:
                return False
        if n > 1:
            return False
        else:
            index = s.find('.')
            front = s[:index]
            behind = s[index + 1:]
            if len(front) == 0 and len(behind) == 0:
                return False
        return True

if __name__ == '__main__':
    s = '+.3E-2'
    print(Solution().isNumeric(s))

