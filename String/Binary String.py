#User function Template for python3


''' Your task to return total number of binary
    substrings in the given string.
    n: Length of string
    s: Given string
'''
def binarySubstring(n,s):
    x = s.count('1')
    return int((x*(x-1))/2)
    
#code here
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        s=str(input())
        print(binarySubstring(n,s))
# } Driver Code Ends
