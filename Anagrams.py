s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
if(len(s1)==len(s2)):
    if(sorted(s1)==sorted(s2)):
        print("True")
    else:
        print("False")
else:
    print("False")