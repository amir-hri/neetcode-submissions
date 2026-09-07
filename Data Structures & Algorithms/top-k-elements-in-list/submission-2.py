import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        n = len(nums)
        nums_heap = []
        ans=[]
        for i in range(n):
            num = nums[i]
            counter[num] = counter.get(num, 0)+1
        #(freq, num) in min heap
        for num in counter.keys():
            heapq.heappush(nums_heap, (counter[num], num))
            if len(nums_heap)>k:
                heapq.heappop(nums_heap)
        for i in range(k):

            ans.append(heapq.heappop(nums_heap)[1])

        return ans