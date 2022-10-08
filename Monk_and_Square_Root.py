t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=0
    for j in range(m):
        if (j*j)%m==n:
            print(j)
            c=1
            break
    if(c==0):
        print(-1)