def majorityElement(A,N):
    import collections
    freqs = collections.Counter(A)
    for k,v in freqs.items():
        if v > N/2:
            return k
    return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            
            print(majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
