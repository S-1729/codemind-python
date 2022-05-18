n=int(input())
sign=1
rev=0
if n<0:
    sign=-1
    n=n*(-1)
while(n!=0):
    rem=n%10
    n//=10
    rev=rev*10+rem
if not -2**31<rev<2**31-1:
    print("0")
else:
    print(sign*rev)