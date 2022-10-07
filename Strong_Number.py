n=int(input())
t=n
sum=0
while(n>0):
    fact=1
    rem=n%10
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
    n//=10
if(t==sum):
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))