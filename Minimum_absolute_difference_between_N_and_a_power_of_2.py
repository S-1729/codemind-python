from math import *
n=int(input())
r,i=0,0
while(r<=n):
    r=2**i
    i+=1
    if(r>n):
        break
l=r//2
print(min(n-l,r-n))
