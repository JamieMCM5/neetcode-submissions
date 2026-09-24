class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)

        sortedKeys = sorted(d, key=d.get, reverse=True)
        res = []
        for i in range(k):
            res.append(sortedKeys[i])

        return res