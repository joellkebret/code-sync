class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        curr = 0
        high = min(height[l],height[r]) * (r-l)

        while l<=r:
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
            curr = min(height[l],height[r]) * (r-l)
            if high < curr:
                high = curr
        return high