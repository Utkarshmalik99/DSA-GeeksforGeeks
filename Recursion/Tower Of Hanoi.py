# User function Template for python3
def toh1(N, fromm, to, aux, moves):
    if N==1:
        print("move disk",N,"from rod",fromm,"to rod",to)
        return moves+1;
    moves = toh1(N-1, fromm, aux, to, moves+1)
    print("move disk",N,"from rod",fromm,"to rod",to)
    moves = toh1(N-1, aux, to, fromm, moves+1)
    return moves

def toh(N, fromm, to, aux):
    # Your code here
    toh1(N, fromm, to, aux, 0)
    return 2**N-1
 
 #{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())
        print(toh(N, 1, 3, 2))

        T -= 1

if __name__ == "__main__":
    main()


# } Driver Code Ends
