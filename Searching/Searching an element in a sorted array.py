def searchInSorted(arr, N, K):
    if K in arr:
        return 1
    else:
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		print(searchInSorted(A,N,K))

# } Driver Code Ends
