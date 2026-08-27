class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        i=0
        j = n-1
        area = 0
        while i<j:
            width = j-i
            height = min(heights[i], heights[j])
            area = max(area, width*height)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return area

