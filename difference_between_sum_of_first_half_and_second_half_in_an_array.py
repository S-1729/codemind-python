n=int(input())
l=list(map(int,input().split()))
sum1,sum2=0,0
for i in l:
    if i<=n/2:
        sum1+=i
    else:
        sum2+=i
print(abs(sum1-sum2))