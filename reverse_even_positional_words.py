s=input()
l=s.split()
for i in range(len(l)):
    if(i%2==0):
        t=l[i]
        print(t[::-1],end=" ")
    else:
        print(l[i],end=" ")