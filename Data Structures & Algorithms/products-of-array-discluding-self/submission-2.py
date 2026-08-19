class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod = [0]*n
        pref = [0]*n
        suff = [0]*n
        pref[0]=suff[n-1]=1
        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1]*nums[i+1]
        for i in range(n):
            prod[i] = pref[i]*suff[i]
        return prod