def reverse_number(x):
    rev = 0
    while x>0:
        rev = rev*10 + (x%10)
        x =x//10
    return rev
class Solution:
    def isPalindrome(self, x: int) -> bool:

        return x == reverse_number(x)
