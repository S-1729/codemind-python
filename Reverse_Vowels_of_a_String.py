string=input()
s=""
l=[]
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        l.append(i)
l=list(reversed(l))
cnt=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        s=s+l[cnt]
        cnt+=1
    else:
        s+=i
print(s)
