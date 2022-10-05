n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if i not in li:
        print(i,end=" ")
        li.append(i)