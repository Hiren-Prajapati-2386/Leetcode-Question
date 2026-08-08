class Solution:
    def romanToInt(self, s: str) -> int:
        RomanToInt = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

        output = 0
        first = 0


        for i in range(len(s) - 1,-1,-1):

            second = RomanToInt[s[i]]

            if second < first:
                output -= second
            else:
                output += second

            first = second

        return output


        