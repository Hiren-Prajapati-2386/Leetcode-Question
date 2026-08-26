class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = -1

        for num in nums:
            if num != val:
                start += 1
                nums[start] = num

        return start + 1
