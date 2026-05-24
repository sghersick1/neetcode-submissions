class Solution:
    def trap(self, height: List[int]) -> int:
        ''' See how much water is held in each stack '''

        total_water = 0
        for i, h in enumerate(height):
            left = 0
            right = len(height) - 1

            # find max column height
            col_height = 0
            while left < i and right > i:
                temp_height = min(height[left], height[right]) - height[i]
                col_height = max(col_height, temp_height)

                # adjust pointers 
                if height[left] <= height[right]:
                    left += 1
                else:
                    right -= 1

            total_water += col_height

        return total_water


            
            