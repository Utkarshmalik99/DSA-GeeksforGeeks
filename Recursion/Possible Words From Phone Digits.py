#User function Template for python3
phone = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def printString(digits,n,res,string="",index=0):
    if index == n:
        res.append(string)
        return
    for i in range(len(phone[digits[index]-2])):
        string += phone[digits[index]-2][i]
        printString(digits,n,res,string,index+1)
        string = list(string)
        string.pop()
        string = ''.join(string)


##Complete this function

def possibleWords(a,N):
    res=list()
    printString(a,N,res)
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        res = possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
