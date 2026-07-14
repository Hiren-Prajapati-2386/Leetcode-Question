class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []
        
        # Iterate through all possible window lengths
        for length in range(2, 10):
            # Iterate through all valid starting positions
            for start in range(10 - length):
                num = int(sample[start:start + length])
                
                # Filter by the given constraints
                if low <= num <= high:
                    result.append(num)
                    
        return result
