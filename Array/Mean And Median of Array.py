#{ 
#Driver Code Starts
#Initial Template for Python 3
import math

# } Driver Code Ends

def median(A,N):
    
    A.sort()
    if (N-1)%2 == 0:
        return (A[(N-1)//2])
    else:
        return (int((A[N//2 - 1] + A[N//2])/2))
    
    
    
def mean(A,N):
    total = sum(A)
    return (int(total/N))

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        print(mean(a,N),median(a,N))
        
        T-=1
    
if __name__=="__main__":
    main()
#} Driver Code Ends
