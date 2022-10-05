n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    c=0
    for j in l:
        if(j<i):
            c+=1
    li.append(c)
for k in li:
    print(k,end=" ")