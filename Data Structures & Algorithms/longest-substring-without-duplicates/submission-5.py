class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Window valid ? grow : shrink
        if len(s) == 0:
            return 0

        longest = 1 
        l, r = 0, 1
        window = {s[l]} 
        while r < len(s):
            right_char = s[r]
            # Shrink
            while right_char in window:
                window.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1

            window.add(right_char)

        return longest