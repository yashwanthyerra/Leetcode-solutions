from collections import Counter
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime = [True]*(n+1)

        prime[0]=False
        prime[1] = False


        i= 2
        while i*i <=n:
            if prime[i]:
                j = i*i
                while j<=n:

                    prime[j] = False

                    j+=i
            i+=1
        prime[n] = False
        freq = Counter(prime)

        return freq[True]




            






        