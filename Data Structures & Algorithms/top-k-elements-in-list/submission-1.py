class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sort = sorted(count, key=count.get, reverse=True)
        res = []
        for i in range(k):
            res.append(sort[i])

        return res