#User function Template for python3

#Complete this function
def printNos(N):
    if N > 0: 
        printNos(N - 1) 
        print(N, end = ' ')
#Your code here
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
