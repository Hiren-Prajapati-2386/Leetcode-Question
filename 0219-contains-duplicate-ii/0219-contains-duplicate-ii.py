class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        window = set()
        left = 0

        for right in range(len(nums)):

            if nums[right] in window:
                return True

            window.add(nums[right])

            if right - left >= k:
                window.remove(nums[left])
                left += 1

        return False