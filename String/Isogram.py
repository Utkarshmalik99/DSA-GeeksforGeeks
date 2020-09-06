def isIsogram(s):
    a=list(s)
    if len(set(a))==len(a):
        return True
    else:
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        if isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
