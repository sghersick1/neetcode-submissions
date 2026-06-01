class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_l, ans_r = -1, -1
        l, r = 0, 0 

        # O(m) - create map of t
        map_t = {}
        for char in t:
            map_t[char] = 1 + map_t.get(char, 0)

        need = len(map_t)
        # O(n) - sliding window through s
        while r < len(s):
            # valid substring ? shrink : grow 
            # O(m) - check substring
            window = {}
            matches = 0
            for i in range(l, r + 1):
                window[s[i]] = 1 + window.get(s[i], 0)
                if s[i] in map_t and window[s[i]] == map_t[s[i]]:
                    matches += 1

            # Valid result
            if matches == need:
                # Update result
                if ans_l == -1 or (r - l) < (ans_r - ans_l):
                    ans_r = r
                    ans_l = l
                l += 1
            else:
                r += 1

            while l < r and s[l] not in map_t:
                l += 1

        return "" if ans_l == -1 else s[ans_l: ans_r + 1]