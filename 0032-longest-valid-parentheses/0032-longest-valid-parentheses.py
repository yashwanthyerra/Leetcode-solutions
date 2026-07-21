class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_lenght = 0

        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "(":
                left +=1
            if s[i] == ")":
                right +=1

            if left==right:
                max_lenght = max(max_lenght,left*2)

            elif right > left:
                left = right =0
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "(":
                left +=1
            if s[i] == ")":
                right +=1

            if left==right:
                max_lenght = max(max_lenght,left*2)

            elif right < left:
                left = right = 0

        return max_lenght


        #  or 
        # def valid_sub_string(s):
            # if s == ")":
            #     return 0
            # stk =[-1]
            # max_lenght = 0
            # for i in range(len(s)):
            #     if s[i] in "(":
            #         stk.append(i)

            #     else:
            #         stk.pop()
            #         if not stk:
            #             stk.append(i)
            #         max_lenght = max(max_lenght, i - stk[-1])


            # return max_lenght


        