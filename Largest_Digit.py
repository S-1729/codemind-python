#largest digit
N=int(input())
large=0
while(N!=0):
    rem=N%10
    N//=10
    if(rem>large):
        large=rem
print(large)  