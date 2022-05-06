#palindome
T = int(input())
for i in range(T):
    n = int(input())
    l = 0
    x=n
    while(n!=0):
        rem=n%10
        l=l*10+rem
        n//=10
    if(l==x):
        print("True")
    else:
        print("False")