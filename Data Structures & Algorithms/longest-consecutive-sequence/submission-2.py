class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # assuming the array is not empty, the lowest answer is 1.
        # [0,0,0,0,5,0,0,0,0] 

        # sort the list, loop through and on each iteration incraese count by 1.
        # if at any point the current value is > 1 more than the previous, stop count.
        # store the value of count and compare it to our current count. 
        # [2,3,4,4,5,10,20]


        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)


        return longest