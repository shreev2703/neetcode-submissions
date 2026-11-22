class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for char in magazine:
           count[char] = count.get(char, 0) + 1
        
        for i in ransomNote:
            if i in count:
                if count[i] == 0:
                    return False
                else:
                    count[i] = count[i] - 1
            else:
                return False
            
        return True