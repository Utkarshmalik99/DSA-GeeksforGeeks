#User function Template for python3
def RecursivePower(n,p):
    if p:
        return (n*RecursivePower(n,p-1)) # recursive call one less power
    return 1
    '''
    return value of n^p recursively;
    '''
    # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def RecursivePower(n,p):
    '''
    return value of n^p recursively;
    '''
    if p: # if power is not 0.
        return (n*RecursivePower(n,p-1)) # recursive call one less power
    return 1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,p = map(int,input().strip().split())
        print(RecursivePower(n,p))
# } Driver Code Ends
