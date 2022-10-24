n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    temp=l[n-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=temp
print(*l)