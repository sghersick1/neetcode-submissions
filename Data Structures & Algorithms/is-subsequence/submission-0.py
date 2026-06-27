class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Clarifying questions
        - So if we were allowed to remove any of characters in t, we could form exactly s
        - Could either s or t be empty?
        - We are only looking for True/False if it is possible?
        - is s is empty, is that considered True: yes
        - are the letters in s and t ALWAYS lower case letters
        
        Edge Cases:
        - empty s
        - empty t
        - contains letters out of order
        - contains letters in order
        - contains multiple copies of letters (t1, t1, x, x, t2, t3, t2, x, x, t4)
        - require first letter
        - require last letter
    
        Brute Force time - O(n), Space - O(1):
        iterate through t, keep pointer to letter in s
        - if t[i] == s[ptr] -> move ptr forward
        - if ptr == len(s) return True
        - if ptr never beats it, return False
    
        Test Cases:
        1. Basic
        s = 'node'
        t = 'neetcode'
        True
    
        2. Empty t
        s = 'node'
        t = ''
    
        3. Both empty
        s = ''
        t = ''
    
        4. Empty s
        s =''
        t ='case'
        """ 
        ptr = i = 0
        size_s, size_t = len(s), len(t)
        while ptr < size_s and i < size_t:
            if t[i] == s[ptr]:
                ptr += 1
            i += 1
    
        return ptr == size_s