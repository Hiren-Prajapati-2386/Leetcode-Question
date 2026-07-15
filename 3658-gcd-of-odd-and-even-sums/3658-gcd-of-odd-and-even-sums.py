class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        sum_even = sum(list(range(2,(2*n)+1,2)))
        sum_odd = sum(list(range(1,(2*n)+1,2)))

        return math.gcd(sum_even,sum_odd)
        