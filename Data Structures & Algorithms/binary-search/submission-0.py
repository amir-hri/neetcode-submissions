class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(r+l)//2
            if target==nums[m]:
                return m
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        return -1