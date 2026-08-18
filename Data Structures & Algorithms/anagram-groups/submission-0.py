class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            sorted_s=''.join(sorted(strs[i]))
            d[sorted_s].append(strs[i])
        return list(d.values())