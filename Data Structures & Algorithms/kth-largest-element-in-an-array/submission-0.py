import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(heap, -1*nums[i])
        for _ in range(k):
            curr = -1*heapq.heappop(heap)
        return curr