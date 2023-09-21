#URL = https://practice.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n4404/1

def prime_Sum(self, r):
    # Code here
    isPrime = [True] * (r + 1)
    isPrime[0] = isPrime[1] = False
    root = int(r ** (1/2))
    for i in range(2, root + 1):
        if isPrime[i]:
            for j in range(i * i, r + 1, i):
                isPrime[j] = False
 
    primeSum = 0
    for i in range(2, r + 1):
        if isPrime[i]:
            primeSum += i
    return primeSum