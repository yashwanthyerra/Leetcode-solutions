def something(n):
    result = []
    while n>0:
        result.append(n%10)
        n=n//10
    dig_pro = 1
    for i in result:
        dig_pro *= i
    
    return dig_pro



class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        
        while True:
            x = something(n)
            if x%t==0:
                return n
                break
            n+=1
        