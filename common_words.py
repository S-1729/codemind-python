s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l1=s1.split()
l2=s2.split()
for i in l2:
    if i in l1:
        print(i,end=" ")