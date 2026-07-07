class Solution:
    def sumAndMultiply(self, n: int) -> int:

        x_str = "".join(char for char in str(n) if char != '0')
        
        if not x_str:
            return 0
            
        x = int(x_str)
        digit_sum = sum(int(char) for char in x_str)
        
        return x * digit_sum