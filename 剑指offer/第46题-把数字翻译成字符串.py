class Solution:
    def GetTranslationCount(self, n):
        if n < 0:
            return
        nStr = str(n)

        return self.getTranslationCount(nStr)

    def getTranslationCount(self, nStr):
        l = len(nStr)
        counts = [0] * l
        for i in range(l - 1, -1, -1):
            if i < l - 1:
                count = counts[i + 1]
                if 10 <= int(nStr[i: i + 2]) <= 25:
                    if i < l - 2:
                        count += counts[i + 2]
                    else:
                        count += 1
            else:
                count = 1
            counts[i] = count
        return counts[0]

    def GetTranslation(self, n):
        if n < 0:
            return
        nStr = str(n)

        return self.getTranslation(nStr)

    def getTranslation(self, nStr):
        l = len(nStr)
        counts = [[]] * l
        for i in range(l - 1, -1, -1):
            if i == l - 1:
                counts[i] = counts[i] + [[nStr[i]]]
            if i == l - 2:
                if 10 <= int(nStr[i: i + 2]) <= 25:
                    counts[i] = [[nStr[i], nStr[i + 1]], [nStr[i:i + 2]]]
                else:
                    counts[i] = [[nStr[i], nStr[i + 1]]]
            if i < l - 2:
                for k in range(len(counts[i + 1])):
                    counts[i] = counts[i] + [counts[i + 1][k]]
                for j in range(len(counts[i])):
                    counts[i][j] = [nStr[i]] + counts[i][j]
                if 10 <= int(nStr[i: i + 2]) <= 25:
                    for n in range(len(counts[i + 2])):
                        counts[i + 2][n] = [nStr[i: i + 2]] + counts[i + 2][n]
                    counts[i] = counts[i] + counts[i + 2]
        return counts

if __name__ == "__main__":
    a = 1213
    print(Solution().GetTranslation(a))
