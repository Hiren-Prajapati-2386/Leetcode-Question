class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums.sort()

        for i,num in enumerate(nums):
            if num == target:
                result.append(i)

        return result
        