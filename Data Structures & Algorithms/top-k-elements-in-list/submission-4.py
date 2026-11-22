class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums)+1)] 

        for i in nums:
            count[i] = count.get(i,0) + 1

        for i, x in count.items(): 
            buckets[x].append(i)
        
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for j in buckets[i]:
                res.append(j)
            if len(res) == k:
                break

        return res
