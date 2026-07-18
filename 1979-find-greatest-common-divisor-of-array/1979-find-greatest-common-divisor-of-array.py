class Solution:
    def findGCD(self, nums: List[int]) -> int:

        min = nums[0]
        max = nums[0]

        for num in nums:
            if num < min:
                min = num
            if num > max:
                max = num

        return math.gcd(min,max)
        