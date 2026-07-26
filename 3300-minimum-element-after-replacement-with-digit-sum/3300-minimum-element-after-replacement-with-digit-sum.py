class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')
        Sum = 0

        for num in nums:
            while(num > 0):
                Sum += num%10
                num //= 10

            min_sum = min(min_sum,Sum)
            Sum = 0
        
        return min_sum


        