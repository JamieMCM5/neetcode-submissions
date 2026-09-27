class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSqrs(n)
            if n == 1:
                return True
        return False
        
    
    def sumOfSqrs(self, n: int) -> int:
        sm = 0
        for i in range(len(str(n))):
            digit = n % 10
            sm += (digit * digit)
            n = n//10
        return(sm)
        

