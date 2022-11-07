n=int(input("enter the number"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i 
    i=i+1
if sum==n:
    print("perfact")
else:
    print("not perfact")



