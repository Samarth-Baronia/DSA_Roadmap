def isDigitSumPalindrome(self,N):
    #code here
    def palin(m):
        original = m
        pal= 0
        while m :
            rem = m % 10
            pal = pal * 10 + rem
            m //= 10
            
        if pal == original :
            return 1
        return 0 
    add  = 0
    while N :
        rem = N % 10 
        add += rem
        N //= 10
    
    return palin(add)