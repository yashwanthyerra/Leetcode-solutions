class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        for i in range(0,len(s)):
            result = set()
            result.add(s[i])

            while i+1<len(s) and s[i+1] not in result:
                result.add(s[i+1])
                i+=1
            max_count = max(max_count,len(result))

        
        return max_count


        