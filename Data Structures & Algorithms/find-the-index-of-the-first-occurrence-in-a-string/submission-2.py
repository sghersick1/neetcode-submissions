class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        amt = len(needle)

        if amt > len(haystack):
            return -1

        for i in range(len(haystack) - amt + 1):
            if needle == haystack[i: i + amt]:
                return i
        return -1