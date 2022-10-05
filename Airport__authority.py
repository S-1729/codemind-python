n=int(input())
l=[]
c1=0
for i in range(n):
    x=int(input())
    l.append(x)
t=int(input())
for i in l:
    if(i<=t):
        c1+=1
    else:
        c1+=2
print(c1)