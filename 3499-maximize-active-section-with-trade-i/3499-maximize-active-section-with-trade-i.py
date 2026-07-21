class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        zero_blocks = []
        one_blocks = []
        
        augmented = '1' + s + '1'
        n = len(augmented)
        
        i = 0
        while i < n:
            if augmented[i] == '1':
                count = 0
                while i < n and augmented[i] == '1':
                    count += 1
                    i += 1
                one_blocks.append(count)
            else:
                count = 0
                while i < n and augmented[i] == '0':
                    count += 1
                    i += 1
                zero_blocks.append(count)
                
        if len(one_blocks) < 3:
            return initial_ones
            
        max_gain = 0
        for i in range(1, len(one_blocks) - 1):
            gain = zero_blocks[i - 1] + zero_blocks[i]
            if gain > max_gain:
                max_gain = gain
                
        return initial_ones + max_gain
