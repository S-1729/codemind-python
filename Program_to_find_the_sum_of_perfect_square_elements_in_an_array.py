import math
n=int(input())
sum=0
l=list(map(int,input().split()))[:n]
for i in l:
    sq=int(math.sqrt(i))
    if(sq*sq==i):
        sum+=i
print(sum)