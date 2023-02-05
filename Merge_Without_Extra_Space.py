t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:m]
    arr=list(sorted(a+b))
    print(*arr)