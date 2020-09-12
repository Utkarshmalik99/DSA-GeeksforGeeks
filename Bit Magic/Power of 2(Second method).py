#if a number n is a power of 2 then bitwise & of n and n-1 will be zero. We can say n is a power of 2 or not based on value of n&(n-1).
#The expression n&(n-1) will not work when n is 0. To handle this case also, our expression will become n& (!n&(n-1))
#Below is the implementation of this method.

def isPowerofTwo(n):
        return (n and (not(n & (n - 1))) ) 

    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

Execution Time:0.58
