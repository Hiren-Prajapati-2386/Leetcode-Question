class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for i in range(1,len(strs)):

            while(strs[i].startswith(prefix) == False):

                prefix = prefix[:len(prefix) - 1]

            if len(prefix) == 0:
                return ""

        return prefix
        