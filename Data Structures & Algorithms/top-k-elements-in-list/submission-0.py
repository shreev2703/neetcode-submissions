class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for x, i in count.items():
            buckets[i].append(x)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
                for o in buckets[i]:
                    res.append(o)
                if len(res)==k:
                    return res
