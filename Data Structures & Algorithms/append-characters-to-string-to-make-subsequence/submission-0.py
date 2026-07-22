class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Questions:
            - Can letters only be appended to the end of s
            - Can s or t be empty?
        
        Edge Cases:
        - s has no characters in t
        - s = t
        - 

        Solution (brute force):
        1. find longest existing subsequence of s, in t
        example:
            coaching -> coding
            c____ing

        simply go through s, track curr_letter in t, count total

        2. Once we know this we can then just return:
            len(t) - subsquence_count

        problems:
        - t has no chars
        """

        ptr_t, ptr_s = 0, 0
        ss_count = 0 # longest subsequence count
        while ptr_t < len(t) and ptr_s < len(s):
            if s[ptr_s] == t[ptr_t]:
                ptr_t += 1
                ss_count += 1

            ptr_s += 1
        return len(t) - ss_count