from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = Counter(s)
        
        
        freq = dict(sorted(d.items(), key=lambda item: item[1],reverse = True))

        r = ""
        for key,value in freq.items():
            r += key*value
                
        return r