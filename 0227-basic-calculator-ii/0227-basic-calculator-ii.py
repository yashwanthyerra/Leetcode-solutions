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
                l.append(ch)

        if num:
            l.append(num)

        n = len(l)//2
        
        def precedance(op):
            if op =="/" or op=="*":
                return 2
            if op =="+" or op=="-":
                return 1
            return 0

        def calculator(l):
            opstk = []
            valstk = []

            for i in l:
                if i.isdigit():
                    valstk.append(int(i))
                else :
                    while opstk and precedance(opstk[-1])>=precedance(i):
                        op = opstk.pop()
                        x = valstk.pop()
                        y = valstk.pop()

                        if op == "/":
                            valstk.append(y//x)
                        elif op == "+":
                            valstk.append(y+x)
                        elif op == "-":
                            valstk.append(y-x)
                        elif op == "*":
                            valstk.append(y*x)
                            

                    opstk.append(i)
            while opstk:
                op = opstk.pop()
                x = valstk.pop()
                y = valstk.pop()
                if op == "/":
                    valstk.append(y//x)
                elif op == "+":
                    valstk.append(y+x)
                elif op == "-":
                    valstk.append(y-x)
                elif op == "*":
                    valstk.append(y*x)
                    
            return valstk[0]
        return calculator(l)