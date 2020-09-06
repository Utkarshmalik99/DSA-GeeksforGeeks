def reverseWords(s):
    tokens = s.split('.')
    rtokens = tokens[::-1]
    return '.'.join(rtokens)

#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

# } Driver Code Ends
