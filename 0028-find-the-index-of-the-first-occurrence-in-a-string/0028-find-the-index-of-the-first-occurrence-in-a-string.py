class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        start = 0
        end = len(haystack) - len(needle) + 1

        for i in range(start,end):
            if(haystack[i:(i + len(needle))] == needle):
                return i

        return -1
        