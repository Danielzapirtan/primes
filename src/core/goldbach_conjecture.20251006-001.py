#! /usr/bin/python3

'''
    Checks Goldbach Conjecture in the range [2**28, 2**29] by brute force.
'''

def pr(p):
    k=3
    while k<=p/k:
        if p%k == 0:
            return False
        k+=2
    return True

def gbn(n):
    p=3
    while p<=n-p:
        if pr(p):
            if pr(n-p):
                return True
        p+=2
    return False

def gbab(a,b):
    n=a
    while n<=b:
        if (gbn(n)==False):
            return False
        n+=2
    return True

if __name__=="__main__":
    import sys
    h=int(sys.argv[1])
    a=2**h
    b=2**(h+1)
    if gbab(a,b) == False:
        print('error', h)
    print(h)


