class Solution:
    def maxArea(self, heights: List[int]) -> int:
                    #im going to use two pointers to check it looks like changing height to a hashmap and using enumerate will probably work best with this because i need indice and value, save the heighest value. need a calculation to find out the most length and min between the lengths for the area and need to return the highest area. 
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
