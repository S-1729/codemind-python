a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum1=sum2=0
for i in range(3):
    if(a[i]>b[i]):
        sum1+=1
    if b[i]>a[i]:
        sum2+=1
print(sum1,sum2)