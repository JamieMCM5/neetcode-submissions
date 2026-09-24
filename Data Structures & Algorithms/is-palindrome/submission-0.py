class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()
        res = ""
        print(word)
        for i in range(len(word)-1, -1, -1):
            res += word[i]

        if word == res:
            return True
        return False

        
