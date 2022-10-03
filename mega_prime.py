def isPrime(k):
    if(k==1 or k==0):
        return False
    for i in range(2,int(k**0.5)+1):
        if(k%i==0):
            return False
    return True

n=int(input())
c,c1,c2=0,0,0
if(isPrime(n)):
    while(n>0):
        rem=n%10
        n//=10
        c+=0
        if(isPrime(rem)==False):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")

    
else:
    print("Not Mega Prime")