class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0

        s = str(num)

        while len(s)>1:
            sum = 0
            for i in s:
                sum += int(i)

            s = str(sum)

        return int(s)
                


        