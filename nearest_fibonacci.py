from math import *
n=int(input())
a,b=0,1
c=a+b
while(c<=n):
    a=b
    b=c
    c=a+b
if(abs(n-c)<abs(n-b)):
    print(c)
elif(abs(n-c)==abs(n-b)):
    print(b,c)
else:
    print(b)