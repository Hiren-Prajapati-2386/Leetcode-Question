class Solution:

    def climbStairs(self, n: int) -> int:

        prev1 = 1
        prev2 = 1

        for i in range(2,n+1):
            current = prev1 + prev2

            prev1 = prev2
            prev2 = current

        return prev2

        
    

#         4
#     3   +     2
#   2 + 1     1  +  0
# 1 + 0

#   2 + 1     1  +   1
#     3   +    2
#         5


# thies is also work but for smull n its normal recursion
# def climbStairs(self, n: int) -> int:

# when n = 0 or 1 mens we at 1 step or at ground so we have only 1 way option 
#         if n == 0 or n == 1:
#             return 1

# mens we when we at 4(n) step what was our step it may be 1 step or(+) 2 step 
#         return self.climbStairs(n-1) + self.climbStairs(n-2)