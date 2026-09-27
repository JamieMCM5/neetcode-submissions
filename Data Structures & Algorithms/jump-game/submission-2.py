class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if i land on a 0, before the end of the list, i cant make it, return false.
        # when i land on a index, i to check all possible jumps and the continuations of those jumps. 
        # [1,2,2,0,0]
        # for this example i can jump to index 1, but then i cant jump to index 3 or i lose, so i have to jump to index 2 first which will then allow
        # me to make the jump to index(-1)
        # a simple base case is that if the number im on = length of the list minus the index, then we can safely jump to the end.
        # so we can start at the last index, which is our goal. iterate backwards and if we can get to our goal from our new index
        # update goal to new index and repeat.

        n = len(nums)
        goal = n - 1

        while goal > 0:
            for i in range(goal - 1, -1, -1):
                diff = goal - i 
                if nums[i] >= diff:
                    goal = i
                elif i == 0:
                    return False
                
        return True