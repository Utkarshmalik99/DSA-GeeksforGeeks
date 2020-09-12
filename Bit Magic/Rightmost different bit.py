{ 
#Driver Code Starts
#Initial Template for Python 3

import math

# } Driver Code Ends
def posOfRightMostDiffBit(m,n):
    def getRightMostSetBit(n):
        return math.log2(n & -n) + 1

    return getRightMostSetBit(m ^ n)

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    
if __name__=="__main__":
    main()
#} Driver Code Ends
