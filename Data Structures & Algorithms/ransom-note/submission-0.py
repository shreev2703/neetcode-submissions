class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counts={}
        
        for char in magazine:
            counts[char] = 1 + counts.get(char,0)
        
        for i in ransomNote:
            if i in counts:
                if counts[i] == 0:
                    return False
                else:
                    counts[i]=counts[i]-1
            else:
                return False
        return True