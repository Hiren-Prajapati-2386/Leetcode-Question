class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = "".join(sorted(s))
        
        if s == sorted_s:
            return 0
        
        if n == 2:
            return -1
        
        min_char = sorted_s[0]
        max_char = sorted_s[-1]
        
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        if s[0] == max_char and s[-1] == min_char:
            has_other_min = any(ch == min_char for ch in s[:-1])
            has_other_max = any(ch == max_char for ch in s[1:])
            if not has_other_min and not has_other_max:
                return 3
                
        return 2