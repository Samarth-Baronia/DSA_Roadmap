#URL = https://practice.geeksforgeeks.org/problems/all-divisors-of-a-number/1


def print_divisors(self, N):
    # code here
    res = []
    root = int(N ** (1/2))
    for i in range (1, root+1):
        if N % i == 0 :
            res.append(i)
            if N/i != i :
                res.append(N//i)
    for i in sorted(res):
        print (i, end= " ")
    