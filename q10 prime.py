
    
a=int(input("enter prime num"))
i=1
count=1
while i<a:
    if a%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("not prime")
    
n=1
while n<=100:
    count=0
    i=2
    t=n//2
    while i<=t:
        if n%i==0:
            count=count+1
        i=i+1
    if count==0 and n!=1:
        print(n,end=" ")
    n=n+1

num=int(input("enter the number :"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("perfact")
else:
     print("not perfact")    


a=int(input("enter the number :"))
b=str(a)
if "0"in b:
    print("duck number")
else:
    print("not")

i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
print(sum)

