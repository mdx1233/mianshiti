class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        dp = [0 for _ in range(len(s))]
        map = dict()
        for i in range(len(s)):
            if s[i] in map:
                if i - map[s[i]] > dp[i-1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = i - map[s[i]]
            else:
                dp[i] = dp[i - 1] + 1
            map[s[i]] = i
        print(dp)
        return max(dp)

    def lengthOfLongestSubstring1(self, s):
        if len(s) < 1:
            return 0
        maxl = 0
        lastl = 0
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                L = i - map[s[i]]
                if L > lastl:
                    lastl += 1
                else:
                    lastl = L
            else:
                lastl += 1
            maxl = max(lastl, maxl)
            map[s[i]] = i
        return maxl

if __name__ == '__main__':
    s = 'arabcacfr'
    print(Solution().lengthOfLongestSubstring(s))
