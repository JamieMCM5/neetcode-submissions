class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        # go through the string
        # if character is a hash tag, take the int conversion of a splice of s[i-1 : i]
        # that should give us the length of the word to take. (might need to add try here incase of 
        # character in the string we actually want being a #)
        # use that length to splice that many indices after the hashtag to get the string and then update i by that amount.


        #s = "5#abcde"
        n = len(s)
        i = 0
        res = []

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1])
            j = j + 1 + length
            i = j

        return res
