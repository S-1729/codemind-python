n=int(input())
l=list(map(int,input().split()))
flag=0
for i in range(n):
    if(l[i]%2!=0):
        flag=1
        break
if(flag==0):
    print("True")
else:
    print("False")