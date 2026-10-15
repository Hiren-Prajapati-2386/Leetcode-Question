class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        Counts = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n+1):

                Counts += len(set(nums[i:j]))**2

        return Counts
        