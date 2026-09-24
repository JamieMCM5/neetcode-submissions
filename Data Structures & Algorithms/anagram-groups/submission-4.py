class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            d[st].append(s)
        
        res = list(d.values())

        return res