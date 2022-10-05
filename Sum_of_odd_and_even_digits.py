n=int(input())
sum1,sum2=0,0
l=list(map(int,input().split()))[:n]
for i in range(len(l)):
    if(i%2==1):
        sum1+=l[i]
    else:
        sum2+=l[i]
if(sum1-sum2==0):
    print("YES")
else:
    print("NO")
    