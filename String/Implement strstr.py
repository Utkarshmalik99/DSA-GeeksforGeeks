def strstr(s,p):
    import re
    loc = re.search(p,s)
    if loc is not None:
        return (loc.start())
    else:
        return -1
    
 #code here
#{ 
#  Driver Code Starts

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

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends
