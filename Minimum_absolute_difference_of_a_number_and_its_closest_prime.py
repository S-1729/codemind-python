from math import *
def isprime(m):
    if(m<=1):
        return False
    for i in range(2,int(sqrt(m))+1):
        if(m%i==0):
            return False
    return True

n=int(input())
i,j=0,0
while(True):
    if(isprime(n+i)):
        break
    else:
        i+=1
while(True):
    if(isprime(n-j)):
        break
    else:
        j+=1
if(i>j):
    print(j)
else:
    print(i)