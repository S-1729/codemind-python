string=input()
s=""
l=[]
for i in string:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        l.append(i)
l=list(reversed(l))
cnt=0
for i in string:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        s=s+l[cnt]
        cnt+=1
    else:
        s+=i
print(s)
