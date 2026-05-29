class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(n)
        for i, el in enumerate(nums):
            if el == target:
                return i

        return -1