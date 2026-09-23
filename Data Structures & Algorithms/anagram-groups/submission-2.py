class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            st = ''.join(sorted(s))
            if st not in seen:
                seen[st] = []
            seen[st].append(s)

        return list(seen.values())