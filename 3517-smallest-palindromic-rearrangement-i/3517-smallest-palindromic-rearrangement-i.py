from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        half_chars = []
        odd_char = ""
        
        for char in sorted(counts.keys()):
            count = counts[char]
            if count % 2 == 1:
                odd_char = char
            half_chars.append(char * (count // 2))
            
        left_half = "".join(half_chars)
        return left_half + odd_char + left_half[::-1]
