class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen = set()
        n = len(s)
        longest=0
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest, len(seen))
        return longest
