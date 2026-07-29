def fac(n):
    if n==1 or n==0:
        return 1
    return n*fac(n-1)
        
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = fac(n)
        count = 0
    
        if x% 10 == 0 :
            while x>0:
                if x%10==0:
                    count+=1
                else:
                    break
                x = x//10

        return count



