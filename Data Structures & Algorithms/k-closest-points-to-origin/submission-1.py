import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist0(x, y):
            return (x**2 + y**2)**(1/2)
        # (dist, point) in min heap based on dist
        heap = []
        ans = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            heapq.heappush(heap, (-dist0(x, y), points[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        for item in heap:
            ans.append(item[1])
        return ans