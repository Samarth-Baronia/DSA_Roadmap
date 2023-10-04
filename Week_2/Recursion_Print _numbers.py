#Question URl = https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

def printNos(self,N):
    #Your code here
    if N == 0 :
        return 
    self.printNos(N-1)
    print (N, end = " ")
