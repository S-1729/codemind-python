t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    sum1=n*(n+1)//2
    sum2=sum(l)
    print(sum1-sum2)