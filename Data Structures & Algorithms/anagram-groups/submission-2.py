class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in range(len(strs)):
            s = tuple(sorted(strs[i]))
            if s not in ans:
                ans[s]=[]
            ans[s].append(strs[i])

        # for i in range(len(strs)):
        #     s = tuple(sorted(strs[i]))
        #     if s in ans:
        #         ans[s].append(strs[i])
        return list(ans.values())
            