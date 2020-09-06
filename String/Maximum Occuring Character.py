def getMaxOccurringChar(s):
    import collections
    freqs = collections.Counter(s)
    maxO = max(freqs.values())
    chars = []
    for c in s:
        if freqs[c] == maxO:
            chars.append(c)
    if len(chars) == 1:
        return chars[0]
    else:
        return min(chars)
    #code here
 
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
        s=str(input())
        print(getMaxOccurringChar(s))
# } Driver Code Ends
