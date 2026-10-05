from collections import Counter
class Solution:


    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        min_len = float("inf")
        start = 0
        t_count = Counter(t)
        window_count = Counter()
        count = 0

        for end in range(len(s)):
            window_count[s[end]] += 1

            if s[end] in t_count and window_count[s[end]] <= t_count[s[end]]:
                count += 1

            while count == len(t):
                curr = end - start +1

                if curr <= min_len:
                    min_len = curr
                    ans = s[start:end+1]

                if s[start] in t_count:
                    window_count[s[start]] -=1
                    if window_count[s[start]] < t_count[s[start]]:
                        count -=1
                start += 1

        return ans