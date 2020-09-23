def isPrime(N):
#Your code here
    if (N <= 1) : 
        return False
    if (N <= 3) : 
        return True
  
# This is checked so that we can skip  
# middle five numbers in below loop 
    if (N % 2 == 0 or N % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= N) : 
        if (N % i == 0 or N % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
