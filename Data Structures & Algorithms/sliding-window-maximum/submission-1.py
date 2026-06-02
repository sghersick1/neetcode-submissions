class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Optimal Sliding Window - O(n)
        result = []
        l = r = 0
        deque = collections.deque()

        while r < len(nums):
            val = nums[r]

            # add val to deque
            while deque and val > deque[-1]:
                deque.pop()
            deque.append(val)

            # update result if full window
            if r - l + 1 == k:
                result.append(deque[0])

            r += 1
            # pop left element if in deque
            if r - l == k:
                if nums[l] == deque[0]:
                    deque.popleft()
                l += 1

        return result