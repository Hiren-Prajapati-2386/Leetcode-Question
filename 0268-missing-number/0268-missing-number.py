class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        end  = len(nums)
        nums = set(nums)
        
        for i in range(start,end+1):
            if i not in nums:
                return i

        return -1
        
# 0 1 2 3 4 5 6 7 _ 9