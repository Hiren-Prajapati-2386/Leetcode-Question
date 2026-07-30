class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first = 0

        if len(s) < 3:
            return True

        for second in range(1,len(s)):

            if s[second] == '1':
                if second - first > 1:
                    return False

                first += 1

        return True
        