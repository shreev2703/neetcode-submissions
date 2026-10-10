class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts={}

        for char in s:
            counts[char]=1+counts.get(char,0)
#counts = {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}


        for i, char in enumerate(s):
            if counts[char]==1:
                return i
            # makes it so the first non repeating is actually 1.
        return -1