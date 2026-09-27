
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        sortedmap = list(sorted(hashmap, key=hashmap.get, reverse=False))


        return sortedmap[0]