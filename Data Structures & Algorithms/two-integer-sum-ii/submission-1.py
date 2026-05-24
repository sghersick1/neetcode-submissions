class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       for l in range(len(numbers)):
        val = numbers[l]
        for r in range(l+1, len(numbers)):
            if numbers[r] + val == target:
                return [l+1, r+1]