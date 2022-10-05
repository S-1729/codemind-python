import math
n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    li.append(i**2)
    
for j in sorted(li):
    print(j,end=" ")