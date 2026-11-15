class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        currentarea = 0
        while left < right:
            area = 0
            length = right - left
            width = min(heights[left], heights[right])
            area = length * width
            currentarea = max(area, currentarea)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return currentarea
