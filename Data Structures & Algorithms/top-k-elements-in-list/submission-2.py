class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sortedcount = sorted(count, key=count.get, reverse=True)
        print(sortedcount)

        res = []
        for i in range(k):
            res.append(sortedcount[i])
        
        return res