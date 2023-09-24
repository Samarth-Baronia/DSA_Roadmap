#URL = https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1

def largest( arr, n):
    maxi = 0 
    for i in arr:
        if i > maxi:
            maxi = i 
    return maxi

