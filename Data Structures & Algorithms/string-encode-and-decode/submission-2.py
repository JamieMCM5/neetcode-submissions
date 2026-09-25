class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)
    def decode(self, s: str) -> List[str]:

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
