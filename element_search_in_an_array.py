n=int(input())
l=list(map(int,input().split()))
k=int(input())
flag=0
for i in range(n):
    if(l[i]==k):
        flag=1
        break
if(flag==1):
    print("True")
else:
    print("False")