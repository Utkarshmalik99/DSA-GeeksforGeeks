def NumberofElementsInIntersection(a,b,n,m):
    return len(set(a).intersection(set(b)))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        
        
        print(NumberofElementsInIntersection(a,b,n,m))
