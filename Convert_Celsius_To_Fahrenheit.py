#{ 
#Driver Code Starts
#Initial Template for Python 3

import math
  # } Driver Code Ends

#User function Template for python3

##Complete this function
def cToF(C):
    return ((9/5)*C + 32)
    #Your code here

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        C=int(input())
        print(math.floor(cToF(C)))
        T-=1
    
    
if __name__=="__main__":
    main()
#} Driver Code Ends
