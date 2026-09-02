class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n-1
        leftmax, rightmax = 0, 0
        total = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax <= rightmax:
                total += leftmax-height[l]
                l+=1
            else:
                total += rightmax-height[r]
                r-=1
        return total
