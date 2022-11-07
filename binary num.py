n=int(input("enter num"))
i=0
sum=0
while n>0:
    rem=n%10
    sum=sum+((2**i)*rem)
    n=n//10
    i=i+1
print(sum)
    