class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="":
            return 0

        l = s.split()
        ans = len(l[-1])

        return ans
        