class Solution:
    def reverse(self, x: int) -> int:

        num = abs(x)
        output = 0

        while(num > 0):
            output = output*10 + (num%10)
            num //= 10

        if x < 0:
            n_output = -output
            if n_output > 2**31 - 1 or n_output < -2**31:
                return 0
            return n_output

        if output > 2**31 - 1 or output < -2**31:
            return 0
        return output

        