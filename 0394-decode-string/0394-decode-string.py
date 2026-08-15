class Solution:
    def decodeString(self, s: str) -> str:
        l=[]
        valstk = []
        alpstk = []
        alp = ""
        num = ""
        for i in range(0,len(s)):

            if s[i].isdigit():
                num+=s[i]
                continue

            if s[i] =="[":
                alpstk.append(alp)
                valstk.append(num)
                num = ""
                alp = ""
                continue

            if s[i].isalpha():
                alp += s[i]

            if s[i]=="]":
                
                x = int(valstk.pop())
                prev = alpstk.pop()
                alp= prev + x*alp

                
                if not valstk:
                    l.append(alp)
                    alp =""
        if alp:
            l.append(alp)
            
        return("".join(l))



        