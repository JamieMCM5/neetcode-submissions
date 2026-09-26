class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        sortednums = list(sorted(hashmap, key=hashmap.get, reverse=True))

        res = []
        for i in range(k):
            res.append(sortednums[i])

        return res

