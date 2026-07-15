class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique_eliment = 0

        for num in nums:
            unique_eliment ^= num
            # use xor gate which work on binary like 101 ^ 011 then 110

        return unique_eliment
        