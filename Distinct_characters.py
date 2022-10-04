s1=input()
s1=s1.lower()
l=[]
for i in s1:
    if i not in l:
        if i!=' ':
            l.append(i)
a=sorted(l)
for i in a:
    print(i,end="")