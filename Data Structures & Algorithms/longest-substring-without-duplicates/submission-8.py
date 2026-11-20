class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
               left = max(map[s[right]]+1,left)
            map[s[right]]=right
            longest = right - left + 1
            res = max(res, longest)
        
        return res