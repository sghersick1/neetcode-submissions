class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Empty String or None
        if not str or len(s) == 0:
            return 0

        longest = 1 
        l = 0 
        while l < len(s) - 1:
            seen = {s[l]} 
            for r in range(l + 1, len(s)):
                if s[r] not in seen:
                    seen.add(s[r])
                else:
                    break
            
            longest = max(longest, len(seen))
            l += 1 
        return longest