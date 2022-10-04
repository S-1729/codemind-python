s=input()
n=int(input())
c1,c2=0,0
l=len(s)
for i in range(l):
    if(s[i]=='a'):
        c1+=1
quo=n//l
rem=n%l
c2=quo*c1
for i in range(rem):
    if(s[i]=='a'):
        c2+=1
print(c2)