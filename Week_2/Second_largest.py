#URL = https://practice.geeksforgeeks.org/problems/second-largest3735/1


def print2largest(self,arr, n):
	# code here
	first = second = -1
	for i in range (0, len (arr)):
	    if arr[i] > first and arr[i] > second :
	        second = first 
	        first = arr[i]
	       
	    if arr[i] > second and arr[i] < first :
	        second = arr[i]
    
    return second