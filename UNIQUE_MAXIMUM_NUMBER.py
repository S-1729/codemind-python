n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if arr.count(i)==1:
        l.append(i)
if(len(l)>0):
    print(max(l))
else:
    print(-1)