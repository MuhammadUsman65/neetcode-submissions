def difference(a, b):
    return a - b

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max =0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                water = min(heights[i],heights[j])*(j-i)
                if water>max:
                    max=water                    
        return max