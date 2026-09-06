class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []

        for char in expression:

            if char in "ft!&|":
                if char == "f":
                    stk.append(False)
                elif char == "t":
                    stk.append(True)
                else:
                    stk.append(char)


            elif char == ")":
                results=[]
                result = True
                while stk and stk[-1] in [True,False]:
                    results.append(stk.pop())
                
                op = stk.pop()

                if op == "!":
                    if results[-1] == True:
                        result = False 
                    else:
                        result = True

                elif op == "&":
                    if len(results) == 1:
                        stk.append(results[0])
                    else:
                        for i in results:
                            result = result and i

                elif op == "|":

                    if len(results) == 1:
                        stk.append(results[0])

                    else:
                        result = False
                        for i in results:
                            result = result or i

                stk.append(result)

        return stk.pop()



            
