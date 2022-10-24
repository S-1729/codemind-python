t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for j in range(k):
        temp=l[n-1]
        for k in range(n-1,0,-1):
            l[k]=l[k-1]
        l[0]=temp
    print(*l)