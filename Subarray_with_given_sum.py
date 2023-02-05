t=int(input())
for k in range(t):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    flag=False
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=l[j]
            if(sum==s):
                print(i+1,j+1)
                flag=True
                break
            if(sum>s):
                break
        if(flag):
            break
    if(flag==False):
        print(-1)