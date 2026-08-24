class Solution:
    def calculate(self, s: str) -> int:
        l = []
        num = ""

        for ch in s:
            if ch.isdigit():
                num += ch

            elif ch == " ":
                continue

            else:
                if num:
                    l.append(num)
                    num = ""

                if ch == "-":

                    # CORRECTED
                    if not l:
                        l.append("0")
                        l.append("-")

                    elif l[-1] == "(":
                        l.append("0")
                        l.append("-")

                    elif l[-1] in ["+", "-", "*", "/"]:
                        num = "-"

                    else:
                        l.append(ch)

                else:
                    l.append(ch)

        if num:
            l.append(num)

        if len(l) == 1 and l[0].isdigit():
            return int(l[0])

            
        def infix_to_post(l):

            stk = []
            result = []
            for ch in l:
                
                if ch.lstrip("-").isdigit():
                    result.append(ch)
                
                elif ch == "(" : 
                    stk.append(ch)
                
                elif ch == ")" :
                    while stk and stk[-1] != "(":
                        result.append(stk.pop())
                    stk.pop()

                else:

                    while (stk and stk[-1] != "(" and precedance(stk[-1])>=precedance(ch)):
                        result.append(stk.pop())

                    stk.append(ch)

            while stk:
                result.append(stk.pop())

            return result
        
        def precedance(op):
            if op=="/" or op == "*":
                return 2
            if op =="+" or op=="-":
                return 1

        def post_fix(expr):
            expr = infix_to_post(expr)
            stk = []
            for ch in expr:
                if ch.lstrip("-").isdigit() : 
                    stk.append(int(ch))
                else:
                    b = stk.pop()
                    a = stk.pop()

                    if ch == "/" :
                        stk.append(a/b)
                    elif ch =="*":
                        stk.append(a*b)
                    elif ch == "+":
                        stk.append(a+b)
                    elif ch == "-":
                        stk.append(a-b)

            return int(stk[0])        

        return post_fix(l)

        