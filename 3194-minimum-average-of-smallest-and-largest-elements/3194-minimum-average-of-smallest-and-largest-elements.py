class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
            nums.sort()
            min_avg = float('inf')
            
            i = 0
            j = len(nums) - 1
            
            while i < j:
                current_avg = (nums[i] + nums[j]) / 2
                if current_avg < min_avg:
                    min_avg = current_avg
                i += 1
                j -= 1
                
            return min_avg