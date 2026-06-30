class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        end  = len(nums)
        
        for i in range(start,end+1):
            if i not in nums:
                return i

        return -1
        