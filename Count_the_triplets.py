t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if l[i]+l[j] in l:
                c+=1
    if c>0:
        print(c)
    else:
        print(-1)
