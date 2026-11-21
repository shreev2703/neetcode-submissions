class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(left, map[s[right]]+1)
            map[s[right]] = right
            longest = right - left + 1
            res = max(longest, res)

        return res