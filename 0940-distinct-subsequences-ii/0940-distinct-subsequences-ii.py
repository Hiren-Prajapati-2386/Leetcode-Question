class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last = [0] * 26
        all_count = 0
        
        for ch in s:
            idx = ord(ch) - ord('a')
            added = (all_count + 1 - last[idx]) % MOD
            all_count = (all_count + added) % MOD
            last[idx] = (last[idx] + added) % MOD
            
        return all_count