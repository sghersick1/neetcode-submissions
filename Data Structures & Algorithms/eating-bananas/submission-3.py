class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Solution
        piles.sort()

        # max_ k
        max_k = math.ceil(len(piles) / h)
        max_k *= piles[-1] 

        # min_k
        min_k = 1 

        ans = max_k
        while min_k <= max_k:
            mid_k = (max_k + min_k) // 2

            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(pile/mid_k)
                 
            if temp_h > h:
                min_k = mid_k + 1
            elif temp_h <= h:
                ans = mid_k
                max_k = mid_k - 1

        return ans