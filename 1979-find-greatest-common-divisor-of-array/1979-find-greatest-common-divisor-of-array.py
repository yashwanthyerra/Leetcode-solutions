def gcd(a,b):
    if b==0:
        return a
    if b>a:
        a,b = b,a
    return gcd(b,a%b)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = max(nums)
        y = min(nums)

        return gcd(x,y)