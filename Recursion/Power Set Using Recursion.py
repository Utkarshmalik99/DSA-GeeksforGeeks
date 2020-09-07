def powerSet(s):
    perm = []
    if len(s) == 0:
        perm.append("")
        return perm
    first = s[0]
    rem = s[1:len(s)]
    words = powerSet(rem)
    perm.extend(words)
    for word in words:
        perm.append(first+word)
    return perm
     
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
# } Driver Code Ends
