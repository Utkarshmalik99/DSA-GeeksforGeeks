def digitalRoot(n):
    '''
    :param n: given number 
    :return: digital root as defined
    '''
    # code here
    while len(str(n)) > 1:
        digits = [int(i) for i in list(str(n))]
        n = sum(digits)
    return n
    
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
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        print(digitalRoot(n))
# } Driver Code Ends
