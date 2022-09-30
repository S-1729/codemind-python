n=int(input())
l=list(map(int,input().split()))
flag=0
arr=[0,1]
for i in range(n):
    if(l[i] not in arr):
        flag=1
        break
if(flag==0):
    print("True")
else:
    print("False")