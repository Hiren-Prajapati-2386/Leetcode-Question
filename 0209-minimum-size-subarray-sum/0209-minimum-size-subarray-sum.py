class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        min_len = float('inf')
        sum_num = 0
    

        for right in range(len(nums)):

            sum_num += nums[right]
            
            while(sum_num >= target):

                min_len = min(min_len,right - left + 1)

                sum_num -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


        