class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d and i!=d[diff]:
                return [i, d[diff]]
                

            