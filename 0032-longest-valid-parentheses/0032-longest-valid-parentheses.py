class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if s == ")":
            return 0
        stk =[-1]
        max_lenght = 0
        for i in range(len(s)):
            if s[i] in "(":
                stk.append(i)

            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                max_lenght = max(max_lenght, i - stk[-1])


        return max_lenght


        