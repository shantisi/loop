n=int (input("enter num"))
b=n
sum=0
while n>0:
    b=n%10
    sum=sum+b
    n=n//10
if n%sum==0:
    print("harshad num")
else:
    print(" not harshad num")