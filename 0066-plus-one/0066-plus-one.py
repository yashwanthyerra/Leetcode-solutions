class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s = s+str(i)

        y = 1 + int(s)
        m = str(y)
        r = []

        for i in range(len(m)):
            r.append(int(m[i]))

        return r

        
        

        