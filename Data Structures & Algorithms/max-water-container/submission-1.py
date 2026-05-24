class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # A = L * W
        # W = idx2 - idx1
        # L = min(height1, height2# A = WL * W

        max_area = -1

        left = 0
        right = len(heights) - 1

        while left < right:
            h1 = heights[left]
            h2 = heights[right]
            length = min(h1, h2)
            width = right - left

            # Update max_area
            if length*width > max_area:
                max_area = length*width

            # Iterate pointers
            if h1 <= h2:
                left += 1
            elif h2 < h1:
                right -= 1

        return max_area 