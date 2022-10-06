n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if(i==l.count(i)):
        if i not in li:
            li.append(i)
print(len(li))