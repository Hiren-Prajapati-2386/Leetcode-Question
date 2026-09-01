class Solution:
    def myAtoi(self, s: str) -> int:

        new_s = s.strip()
        
        if len(new_s) == 0:
            return 0

        negative = True if new_s[0] == "-" else False
        positive = True if new_s[0] == "+" else False

        output = 0


        for i in range(len(new_s)):

            if (i == 0 and negative) or (i == 0 and positive):
                continue

            if '0' <= new_s[i] <= '9':
                output = output*10 + int(new_s[i])
            else:
                break

        if negative:
            n_output = -output
            if n_output < -2**31:
                return -2**31
            return n_output

        if output > 2**31-1:
            return 2**31 - 1

        return output



        