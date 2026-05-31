class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 1
        l, r = 0, 0
        mp = {}

        # O(n)
        while r < len(s):
            if s[r] not in mp:
                mp[s[r]] = 0
            mp[s[r]] += 1

            # O(26)
            while True:
                max_char_amt = 0
                for key, value in mp.items():
                    max_char_amt = max(max_char_amt, value)
    
                if (r - l + 1) - max_char_amt <= k:
                    break
                else:
                    mp[s[l]] -= 1
                    l += 1

            # Grow window
            result = max(result, (r -l + 1))
            r += 1

        return result
