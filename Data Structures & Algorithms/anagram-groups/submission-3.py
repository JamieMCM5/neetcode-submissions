class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a hashmap that uses the sorted words as keys and stores a list of the words matching that sorted word as values. defaultdict allows us to do this without an if statement to check whether the word is contained in the dict.

        mydict = defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            mydict[st].append(s)

        sortedstrs = list(mydict.values())
        return sortedstrs