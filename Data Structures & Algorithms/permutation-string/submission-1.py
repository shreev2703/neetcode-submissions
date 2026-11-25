class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if lens1 > lens2:
            return False

        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(0, lens1):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        if s1count == s2count:
            return True

        left = 0
        for right in range(lens1,lens2):
            s2count[ord(s2[right]) - ord("a")] += 1
            s2count[ord(s2[left]) - ord("a")] -= 1

            left += 1

            if s1count == s2count:
                return True

        return False
