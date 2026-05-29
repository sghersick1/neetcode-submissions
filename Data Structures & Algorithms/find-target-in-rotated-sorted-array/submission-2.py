class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            val = nums[m]

            if val == target:
                return m
            
            if val > target and nums[l] <= target:
                r = m - 1
            elif val < target and nums[r] >= target:
                l = m + 1
            elif val > target and nums[l] > target:
                l += 1 
            elif val < target and nums[r] < target:
                r -= 1 
                
        return -1