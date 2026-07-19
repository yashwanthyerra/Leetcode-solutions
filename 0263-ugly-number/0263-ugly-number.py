class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0 or n==-1:
            return False
        
        
        while n%2==0:
            n//=2
        while n%5==0:
            n//=5
        while n%3==0:
            n//=3

        return n==1 
        