class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == "(":
                depth += 1
            else:
                depth -= 1
                # Only add when we find a leaf "()"
                if s[i - 1] == "(":
                    score += 1 << depth

        return score


        