
def get_value(item):
    return (-item[1],item[0])
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
            freq  = {}

            for word in words:
                if word in freq:
                    freq[word] += 1

                else:
                    freq[word] = 1 

            sorted_d = dict(sorted(freq.items(),key = get_value))


            l = list(sorted_d.keys())
            return l[:k]