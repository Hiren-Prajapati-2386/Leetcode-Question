class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


# sliding windows method to find avg
        max_sum = sum(nums[:k])
        max_avg = max_sum/k

        for i in range(k,len(nums)):

            max_sum = max_sum - nums[i-k] + nums[i]
            max_avg = max(max_avg,max_sum/k)

        return max_avg

        