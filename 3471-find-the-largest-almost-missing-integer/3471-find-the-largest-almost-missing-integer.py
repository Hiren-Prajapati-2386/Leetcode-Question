class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = defaultdict(int)
        
        for i in range(n - k + 1):
            unique_elements = set(nums[i:i+k])
            for x in unique_elements:
                counts[x] += 1
                
        ans = -1
        for x, count in counts.items():
            if count == 1:
                if x > ans:
                    ans = x
                    
        return ans
