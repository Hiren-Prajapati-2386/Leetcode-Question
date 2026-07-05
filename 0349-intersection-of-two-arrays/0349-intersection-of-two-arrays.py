class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2 = set(nums2)
        nums1 = list(set(nums1))

        for num in nums1:
            if num in nums2:
                result.append(num)

        return result

        