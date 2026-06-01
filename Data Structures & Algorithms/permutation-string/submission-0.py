class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create map of characters for permutation
        perm = {}

        # O(m) - length of s1 
        for char in s1:
            if char not in perm:
                perm[char] = 0
            perm[char] += 1

        # window length always = len(s1)
        l, r = 0, len(s1) - 1
        # O(n) - length of s2
        while r < len(s2):
            perm_check = {}
            valid = True
            # O(m) - check if permuatation
            for i in range(l, r + 1):
                char = s2[i]
                if char not in perm_check:
                    perm_check[char] = 0
                perm_check[char] += 1

                if char not in perm or perm_check[char] > perm[char]:
                    valid = False
                    break

            if valid == True:
                return True
            
            # Inc window
            l += 1
            r += 1
            
        return False