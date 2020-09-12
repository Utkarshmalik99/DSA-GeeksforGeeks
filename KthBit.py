#{ 
#Driver Code Starts
#Initial Template for Python 3

import math

 # } Driver Code Ends

def checkKthBit(n,k):
    if (n & (1<<k)!=0):
        return True
    else:
        return False

#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
