def grayToBinary(n):
    inv = 0
    while (n):
        inv = inv ^ n
        n = n >> 1
    return inv

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
