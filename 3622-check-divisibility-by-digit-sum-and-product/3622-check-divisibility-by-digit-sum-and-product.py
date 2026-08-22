class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp =n
        x = n
        result1 = 0

        while n>0:
            result1 += n%10

            n = n//10

        result2 = 1

        while x>0:
            result2 *= x%10

            x = x//10

        m = result1 + result2

        return (temp%m==0)
        