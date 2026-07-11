class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = sorted(s)
        t = sorted(t)

        for a, b in zip(s, t):
            if a != b:
                return b

        return t[-1]
        