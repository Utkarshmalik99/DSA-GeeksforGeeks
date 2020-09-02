#User function Template for python3
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
#User function Template for python3
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
        
