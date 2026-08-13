class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) <=1:
            if s[0]=="*":
                return ""
            else:
                return s
        stk = []
        for i in s :
            if i!="*":
                stk.append(i)
            else:
                stk.pop()


        j = "".join(stk)
        return j
        