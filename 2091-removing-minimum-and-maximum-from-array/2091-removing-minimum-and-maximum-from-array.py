class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        min_index = 0
        max_index = 0

        # Find indexes of minimum and maximum
        for i in range(n):
            if nums[i] < nums[min_index]:
                min_index = i

            if nums[i] > nums[max_index]:
                max_index = i

        # Put them in left-to-right order
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 3 possible strategies
        from_front = right + 1
        from_back = n - left
        both_sides = (left + 1) + (n - right)

        return min(from_front, from_back, both_sides)