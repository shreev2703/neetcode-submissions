class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use the sliding window technique and put the first pointer at the start and the second at the second 
        left = 0
        setS=set()
        res=0

        for right in range(len(s)):
            while s[right] in setS:
                setS.remove(s[left])
                left += 1
            setS.add(s[right])
            res = max(res, right - left + 1)
        
        return res