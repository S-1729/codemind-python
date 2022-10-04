s1=input()
s1=s1.lower()
l=[]
for i in s1:
    if s1.count(i)==1 and i!=' ':
        l.append(i)
if(len(l)>0):
    print(l[0])
else:
    print("-1")