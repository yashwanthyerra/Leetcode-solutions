class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num)//2

        left = num[:mid]
        right = num[mid:]

        q1 = left.count("?")
        q2 = right.count("?")

        sum1 = sum(int(x) for x in left if x.isdigit())
        sum2 = sum(int(x) for x in right if x.isdigit())

        if (q1 + q2) % 2 != 0:
            return True

        return sum1 - sum2 != 9 * (q2 - q1) // 2
        