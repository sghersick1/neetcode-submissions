class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        result = (-1, -1)

        # O(m) - create map of t
        map_t = {}
        for char in t:
            map_t[char] = 1 + map_t.get(char, 0)
        
        have, need = 0, len(map_t)
        window = {}
        while r < len(s):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # update have
            if char in map_t and window[char] == map_t[char]:
                have += 1

            # valid ?
            while have == need:
                # update result ?
                if result[0] == -1 or (result[1] - result[0]) > r - l:
                    result = (l, r)
                
                # shrink 
                window[s[l]] -= 1
                if s[l] in map_t and window[s[l]] < map_t[s[l]]:
                    have -= 1

                l += 1
            else:
                # grow
                r += 1 

        return "" if result[0] == -1 else s[result[0]:result[1] + 1]
