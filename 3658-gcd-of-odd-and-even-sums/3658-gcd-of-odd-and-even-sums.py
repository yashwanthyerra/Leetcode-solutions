def gcd(a,b):
    if b==0:
        return a
    if b>a:
        a,b = b,a
    return gcd(b,a%b)
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        x = [i for i in range(2*n+1) if i%2!=0]

        y = [i for i in range(2*n+1) if i%2==0]

        s = sum(x)
        t = sum(y)

        return gcd(s,t)
        