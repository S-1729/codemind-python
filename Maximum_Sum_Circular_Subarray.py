from math import *
n=int(input())
l=list(map(int,input().split()))
cmax,maxs=l[0],l[0]
cmin,mins=l[0],l[0]
summ=sum(l)
for i in range(1,n):
    cmax=max(cmax+l[i],l[i])
    maxs=max(cmax,maxs)
    cmin=min(cmin+l[i],l[i])
    mins=min(cmin,mins)
if(mins==summ):
    print(maxs)
else:
    print(max(maxs,summ-mins))