s=input()
l=s.split()
for i in range(len(l)-1,-1,-1):
    t=l[i]
    print(t[::-1],end=" ")