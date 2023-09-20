#URL = https://practice.geeksforgeeks.org/problems/count-digits5716/1

def evenlyDivides (self, N):
    # code here
    test = N
    c = 0
    while N:
        rem = N % 10
        if rem == 0 :
            N //= 10
            continue
        if test % rem == 0 :
            c += 1
        N //= 10
    return c