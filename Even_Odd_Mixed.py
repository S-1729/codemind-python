n=int(input())
c=len(str(n))
e,o=0,0
while(n>0):
    rem=n%10
    n//=10
    if(rem%2==0):
        e+=1
    else:
        o+=1
if(e==c):
    print("Even")
elif(o==c):
    print("Odd")
else:
    print("Mixed")