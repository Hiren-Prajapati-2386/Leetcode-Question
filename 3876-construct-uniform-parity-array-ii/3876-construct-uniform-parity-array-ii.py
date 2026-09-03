class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # two condition most imp
        # 1.if all even then array num2 even so true
        # 2.if we have odd in array then min_eliment of array is most odd

        min_eliment = min(nums1)

        if min_eliment % 2 == 1:
            return True

        return all(x % 2 == 0 for x in nums1)
        