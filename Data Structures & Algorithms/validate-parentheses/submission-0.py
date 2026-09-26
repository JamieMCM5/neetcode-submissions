class Solution:
    def isValid(self, s: str) -> bool:
        # if we use a stack, we can check if our current bracket is closed by seeing
        # if the previous item in the stack is an opening bracket of same type
        # go through the string, add the bracket and check if the last added value can close it
        # if so, pop both. 

        # maybe use a dict to keep the valid pairs 

        stack = []
        valid = {")" : "(", "}" : "{","]" : "["}

        for c in s:
            if c in valid:
                if stack and stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)




        if not stack:
            return True
        else:
            return False