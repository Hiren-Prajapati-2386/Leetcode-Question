class Solution:
    def isValid(self, s: str) -> bool:

        opening = {'(','{','['}
        closing = {')','}',']'}
        openToclose = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []

        for ch in s:
            if ch in closing:
                if len(stack) == 0:
                    return False
                if ch == openToclose[stack[-1]]:
                    stack.pop()
                else:
                    return False

            elif ch in opening:
                stack.append(ch)

        return True if len(stack) == 0 else False


        