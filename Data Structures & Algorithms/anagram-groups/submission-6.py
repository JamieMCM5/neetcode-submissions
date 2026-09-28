class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            hashmap[st].append(s)
        
        return list(hashmap.values())
        