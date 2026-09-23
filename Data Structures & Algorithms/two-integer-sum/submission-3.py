class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bigmap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in bigmap:
                return [bigmap[difference], index]
            bigmap[value] = index

        return []