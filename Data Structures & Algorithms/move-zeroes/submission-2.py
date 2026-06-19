class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0 
        while l < len(nums):
            r = l
            while nums[l] == 0:
                if nums[r] != 0:
                    tmp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = tmp
                    break
                elif r == len(nums) - 1:
                    return
                r += 1
            l += 1