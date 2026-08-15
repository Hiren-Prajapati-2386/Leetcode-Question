class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):

            ch = s[right]
            seen[ch] = seen.get(ch,0) + 1

            while(seen[ch] > 2):
                left_ch = s[left]
                seen[left_ch] -= 1
                left += 1

            max_len = max(max_len,right-left+1)

        return max_len


        