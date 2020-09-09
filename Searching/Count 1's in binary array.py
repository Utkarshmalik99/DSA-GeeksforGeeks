def countOnes(arr, N):
    return arr.count(1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            
            print(countOnes(A,N))
            
            T-=1

if __name__ == "__main__":
    main()
# } Driver Code Ends
