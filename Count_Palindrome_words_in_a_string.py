s=input()
l=s.split()
c=0
for i in range(len(l)):
    l[i]=l[i].lower()
    temp=l[i]
    if(l[i]==temp[::-1]):
        c+=1
print(c)