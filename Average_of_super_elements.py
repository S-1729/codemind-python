n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if(i==l.count(i) and i not in li):
        li.append(i)
if(len(li)==0):
    print("-1")
else:
    print("{:.2f}".format(sum(li)/len(li)))