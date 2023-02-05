t=int(input())
l=list(map(int,input().split()))[:t]
n=int(input())
for i in range(n):
    print(l[i],end=" ")
    print(l[n+i],end=" ")