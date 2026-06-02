class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force - O(n^2)
        l, r = 0, k
        result = []
        mp = {}

        # O(n)
        while r <= len(nums):
            # find window max - O(n)
            high = nums[l]
            for i in range(l, r):
               high = max(high, nums[i]) 

            result.append(high)
            l += 1
            r += 1

        return result
