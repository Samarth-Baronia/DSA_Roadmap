#Question URl = https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1

def printNos(self, n):
    # Code here
    if n == 0 :
        return
    print (n, end = " ")
    self.printNos(n-1)