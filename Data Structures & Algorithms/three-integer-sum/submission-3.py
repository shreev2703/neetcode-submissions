class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, x in enumerate(nums):
            if x > 0:
                break
            if i>0 and x == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1

            while left < right:
                threesum = x + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                elif threesum == 0:
                    res.append([x, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left]==nums[left-1]:
                        left += 1
        return res