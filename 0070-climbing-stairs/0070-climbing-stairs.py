def fac(y):
    if y==1 or y==0:
        return 1
    return y * fac(y-1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 :
            return 1

        count = 1

        
        for i in range(1,n//2 +1):
            count += fac(n-i)//((fac(i))*(fac(n-(2*i))))

        

        return count


        
        