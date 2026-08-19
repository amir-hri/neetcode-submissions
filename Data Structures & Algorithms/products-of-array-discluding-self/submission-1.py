class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod = [1]*n
        prefix = 1
        for i in range(n):
            prod[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            prod[i] *= suffix
            suffix *= nums[i]
        return prod