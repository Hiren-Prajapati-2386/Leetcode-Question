class Solution:
    def romanToInt(self, s: str) -> int:

        romanToInt  = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        output = 0
        pri = 0

        for i in range(len(s)-1,-1,-1):

            if((pri == 5 or pri == 10) and s[i] == 'I'):
                pri = 1
                output -= 1
            elif((pri == 50 or pri == 100) and s[i] == 'X'):
                pri = 10
                output -= 10
            elif((pri == 500 or pri == 1000) and s[i] == 'C'):
                pri = 100
                output -= 100
            else:
                output += romanToInt[s[i]]
                pri = romanToInt[s[i]]


        return output

        