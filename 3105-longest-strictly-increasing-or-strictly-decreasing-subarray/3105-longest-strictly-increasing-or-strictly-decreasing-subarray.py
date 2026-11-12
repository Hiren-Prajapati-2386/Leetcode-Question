class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        increas = 1
        decreas = 1
        max_len = 1

        for i in range(0,len(nums)-1):

            if nums[i] > nums[i+1]:
                increas += 1
                decreas = 1
            elif nums[i] < nums[i+1]:
                decreas += 1
                increas = 1
            else:
                increas = 1
                decreas = 1

            max_len = max(max_len,increas,decreas)

        return max_len

        