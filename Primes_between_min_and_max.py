def isPrime(i):
    if(i==1):
        return False
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return False
    return True
c=0
n=int(input())
l=list(map(int,input().split()))
a=l.index(min(l))
b=l.index(max(l))
if(a<b):
    for i in range(a,b+1):
        if(isPrime(l[i])):
            c+=1
else:
    for i in range(b,a+1):
        if(isPrime(l[i])):
            c+=1
print(c)