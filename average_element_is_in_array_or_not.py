n=int(input())
l=list(map(int,input().split()))
sum=0
flag=0
for i in range(n):
    sum+=l[i]
avg=sum//n
for i in range(n):
    if(l[i]==avg):
        flag=1
        break
if(flag==1):
    print("True")
else:
    print("False")