n=int(input())
def reverse(n):
    sum=0
    sign=1
    if(n<0):
        sign=-1
        n=n*-1
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n//=10
    if not -2147483648<sum<2147483647:
        return 0
    return sign*sum
print(reverse(n))