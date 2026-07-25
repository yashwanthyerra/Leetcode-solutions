class Solution:
    def maxProduct(self, n: int) -> int:

        l =[]
        while n>0:
            l.append(n%10)
            n = n//10

        x = max(l)
        l.pop(l.index(x))
        y=max(l)

        return x*y
        