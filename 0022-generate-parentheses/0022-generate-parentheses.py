class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        result = []


        def backtracking(openN,closeN):

            # if closeN == openN == n mens its valid parentheses and we can use as result
            if closeN == openN == n:
                result.append("".join(stack))
                return


            # we can only add one parentheses if open < n
            if openN < n:
                stack.append('(')
                backtracking(openN+1,closeN)
                stack.pop()

            # we can only add closing parentheses if closeN < openN or parentheses

            if closeN < openN:
                stack.append(')')
                backtracking(openN,closeN+1)
                stack.pop()

        backtracking(0,0)
        return result
        