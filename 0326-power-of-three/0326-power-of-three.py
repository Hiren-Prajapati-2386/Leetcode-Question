class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        MAX_POWER_OF_THREE = 3**39
        return n > 0 and MAX_POWER_OF_THREE % n == 0
        