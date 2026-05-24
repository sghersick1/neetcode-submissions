class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # A = L * W
        # W = idx2 - idx1
        # L = min(height1, height2# A = WL * W

        max_area = -1

        # brute force
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                W = abs(i-j)
                L = min(h1, h2)
                area = L * W

                max_area = max(max_area, area)

        return max_area 