n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if(i==l.count(i)):
        li.append(i)
if(len(li)==0):
    print(-1)
else:
    print(min(li),end=" ")
    print(max(li))