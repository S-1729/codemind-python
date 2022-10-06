n=int(input())
l=list(map(int,input().split()))
k=int(input())
li=[]
for i in l:
    if(k==l.count(i)):
        if i not in li:
            li.append(i)
if(len(li)==0):
    print(-1)
else:
    print(*li)