n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if l.count(i)==1:
        li.append(i)
if(len(li)>0):
    print(*li)
else:
    print(-1)