class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen={}
        for i, x in enumerate(nums):
            if x in seen and abs(i-seen[x])<=k:
                return True
            else:
                seen[x]=i
        return False