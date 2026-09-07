class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        n = len(nums)
        ans = []
        for i in range(n):
            num = nums[i]
            counter[num] = counter.get(num, 0)+1
        for i in range(k):
            currmax = max(counter, key=counter.get)
            ans.append(currmax)
            del counter[currmax]
        return ans