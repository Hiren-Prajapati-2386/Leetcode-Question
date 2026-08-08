class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        opening = {'(','[','{'}
        closing = {')',']','}'}

        dict_par = {'(' : ')',
                    '{' : '}',
                    '[' : ']'}

        for i in s:

            if i in opening:
                stack.append(i)

            elif i in closing:

                if len(stack) == 0:
                    return False

                if(dict_par[stack[-1]] == i):
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
        