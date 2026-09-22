class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax, summax = nums[0], nums[0]
        for num in nums[1:]:
            currmax = max(num, currmax+num)
            summax = max(currmax, summax)

        return summax
        