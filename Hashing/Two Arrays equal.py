def check(arr1, arr2, n):
    if set(arr1)==set(arr2):
        return 1
    else:
        return 0
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        n=int(input())
        
        arr1 = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        if check(arr1, arr2, n):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
