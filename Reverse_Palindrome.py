def isPalindrome(i):
    temp=int(str(i)[::-1])
    if(temp==i):
        return True
    return False
n=int(input())
while(True):
    rev=str(n)[::-1]
    res=n+int(rev)
    if(isPalindrome(res)):
        print(res)
        break
    else:
        n=res
        