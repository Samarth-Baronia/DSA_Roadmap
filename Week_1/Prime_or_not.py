def isPrime (N):
    # code here
    if N == 1 :
        return 0
    J = int(N**(1/2))
    for i in range (2, J + 1):
        if N % i == 0 :
            return 0
    return 1

print(isPrime(11))
