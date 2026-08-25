class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lmax=1
        curr=1
        nums_s = sorted(set(nums))
        for i in range(1, len(nums_s)):
            if nums_s[i] - nums_s[i-1] == 1:
                curr+=1
            else:
                curr=1
            lmax=max(lmax,curr)
        return lmax
