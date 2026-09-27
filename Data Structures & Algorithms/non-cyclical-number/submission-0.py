class Solution:
    def isHappy(self, n: int) -> bool:
        # 123 % 10
        # last = 3^2
        # 123 // 10 = 12
        # 12 % 10 = 2
        # next = 2^2
        # 12 // 10 = 1
        #first = 1 ^
        # sum = last + next + first (9 + 3 + 1) = 13
        # hashset = (123, 13, ..)#
        # if the digit we're processing is in the set, loop wiill be infinite, return false
        # if the digit = 1, return True.
    
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSqrs(n)
            if n == 1:
                return True
        return False
        
    
    def sumOfSqrs(self, n: int):
        sm = 0
        for i in range(len(str(n))):
            digit = n % 10
            sm += (digit * digit)
            n = n//10
        return(sm)
        

