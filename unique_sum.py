n=int(input())
l=list(map(int,input().split()))
li=[]
sum=0
for i in l:
    if i not in li:
        li.append(i)
        sum+=i
print(sum)