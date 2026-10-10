class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        threshold=len(nums)//2

        for num in nums:
            counts[num]=1+counts.get(num,0)

        for i in counts:
            if i in counts:
                if counts[i]>threshold:
                    return i