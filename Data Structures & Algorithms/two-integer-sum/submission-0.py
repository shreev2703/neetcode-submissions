class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, x in enumerate(nums):
            complement=target-x
            if complement in seen:
                j=seen[complement]
                if [j]>[i]:
                    return[i,j]
                else:
                    return[j,i]
            else:
                seen[x]=i