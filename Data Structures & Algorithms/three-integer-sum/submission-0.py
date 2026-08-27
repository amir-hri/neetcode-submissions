class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            target = (-1) * nums[i]
            while k>j:
                curr_sum = nums[j]+nums[k]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif curr_sum < target:
                    j+=1
                else:
                    k-=1
        return res