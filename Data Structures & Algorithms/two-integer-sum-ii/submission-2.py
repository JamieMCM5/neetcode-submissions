class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i want to use binary search to find the remainder of the current value
        # so loop through values, for each loop search for the answer, if exists -> true.
        

        l, r = 0, len(numbers) - 1

        while l < r:
            cSum = numbers[l] + numbers[r]
            if target > cSum:
                l += 1
            elif target < cSum: 
                r -= 1
            else:
                return [l + 1, r + 1]