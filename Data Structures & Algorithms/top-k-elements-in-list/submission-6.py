class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sortedval = list(sorted(count, key=count.get, reverse=True))
        for i in range(k):
            result[i] = sortedval[i]

        return result