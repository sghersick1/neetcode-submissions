class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums - O(nlg(n))
        nums.sort()

        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            val1 = nums[i]

            # 2sum (two pointer method)
            l = i+1
            r = len(nums)-1

            while l < r:
                val2 = nums[l]
                val3 = nums[r]
                sum = val1 + val2 + val3

                if sum == 0:
                    res.append([val1, val2, val3])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1

        return res
