class Solution:
    def countCommas(self, n: int) -> int:
        comma_count = 0
        x = 1000
        while x<=n:
            comma_count += n-x+1
            x  = x * 1000
        return comma_count