class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r-1:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m

        # check final case
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l

        return -1